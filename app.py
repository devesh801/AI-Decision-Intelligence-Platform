
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from insights.decision_engine import DecisionEngine

from graph.workflow import graph
from ml.profiler import DataProfiler
from ml.quality import DataQualityAnalyzer
from ml.cleaner import DataCleaner
from ml.strategy_engine import StrategyEngine
from automl.engine import AutoMLEngine
from insights.executive_summary import ExecutiveSummary

st.set_page_config(page_title="AI Decision Intelligence Platform",
                   page_icon="🤖",
                   layout="wide")

st.title("🤖 AI Decision Intelligence Platform")
st.markdown("### AI Research + Machine Learning + Decision Intelligence")

research_tab, ml_tab, reports_tab = st.tabs(
    ["🤖 Research", "📊 ML Studio", "📂 Reports"]
)

with research_tab:
    st.header("Research Assistant")
    topic = st.text_input("Enter Research Topic")
    if st.button("Generate Research"):
        if topic.strip():
            result = graph.invoke({"topic": topic})
            st.session_state["research_report"] = result["final_report"]
            st.success("Research Completed!")
            st.subheader("📄 AI Research Report")
            st.write(result["final_report"])
        else:
            st.warning("Please enter a topic.")

with ml_tab:
    st.header("📊 Machine Learning Studio")
    uploaded_file = st.file_uploader("Upload CSV Dataset", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)
        st.success("Dataset Uploaded Successfully")
        st.dataframe(df.head())

        profiler = DataProfiler()
        profile = profiler.profile(df)

        quality = DataQualityAnalyzer().analyze(df)
        clean_df = DataCleaner().clean(df)

        st.divider()
        st.header("📊 Dataset Profile")
        c1,c2,c3 = st.columns(3)
        c1.metric("Rows", profile["rows"])
        c2.metric("Columns", profile["columns"])
        c3.metric("Memory (KB)", profile["memory_usage_kb"])

        st.divider()
        st.header("🧹 Clean Dataset")
        st.dataframe(clean_df.head())

        st.divider()
        st.header("🔥 Correlation Heatmap")
        numeric_df = clean_df.select_dtypes(include=["number"])
        if numeric_df.shape[1] > 1:
            fig, ax = plt.subplots(figsize=(7,5))
            im = ax.imshow(numeric_df.corr())
            plt.colorbar(im)
            ax.set_xticks(range(len(numeric_df.columns)))
            ax.set_xticklabels(numeric_df.columns, rotation=90)
            ax.set_yticks(range(len(numeric_df.columns)))
            ax.set_yticklabels(numeric_df.columns)
            st.pyplot(fig)

        st.divider()
        target = st.selectbox("🎯 Target Column", clean_df.columns)

        strategy = StrategyEngine().recommend(profile, quality, target, clean_df)

        st.header("🧠 AI Strategy")
        st.write(f"**Problem Type:** {strategy['problem_type']}")
        st.write(f"**Metric:** {strategy['metric']}")

        st.subheader("Recommended Models")
        for m in strategy["models"]:
            st.write("⭐", m)

        st.divider()
        st.header("🤖 AutoML")

        if st.button("🚀 Train Models"):
            try:
                X = clean_df.drop(columns=[target])
                st.session_state["feature_columns"] = X.columns.tolist()
                y = clean_df[target]

                automl = AutoMLEngine()
                leaderboard, problem_type, trained_model = automl.train(X, y)
                st.session_state["trained_model"] = trained_model
                st.session_state["leaderboard"] = leaderboard
                st.session_state["best_model"] = leaderboard[0]
                st.session_state["problem_type"] = problem_type
                st.session_state["model_trained"] = True

                st.session_state["trained_model"] = trained_model
                st.session_state["feature_columns"] = X.columns.tolist()

                best_model = leaderboard[0]

                st.success("✅ Training Completed Successfully!")
                st.subheader("🏆 Model Leaderboard")
                st.dataframe(pd.DataFrame(leaderboard), use_container_width=True)

                st.success(f"🏆 Best Model: {best_model['Model']}")

                summary = ExecutiveSummary().generate(best_model, problem_type)

                st.header("📋 Executive Summary")
                st.write(summary)
                if problem_type == "Classification":
                    st.metric("Accuracy", best_model["Accuracy"])
                    st.metric("Precision", best_model["Precision"])
                    st.metric("Recall", best_model["Recall"])
                    st.metric("F1 Score", best_model["F1 Score"])
                    st.subheader("Confusion Matrix")
                    st.dataframe(pd.DataFrame(best_model["Confusion Matrix"]))
                else:
                    c1,c2,c3 = st.columns(3)
                    c1.metric("R²", best_model["R2 Score"])
                    c2.metric("MAE", best_model["MAE"])
                    c3.metric("RMSE", best_model["RMSE"])

                if best_model.get("Feature Importance"):
                    imp = pd.DataFrame(
                        list(best_model["Feature Importance"].items()),
                        columns=["Feature","Importance"]
                    ).sort_values("Importance", ascending=False)
                    st.subheader("Feature Importance")
                    st.dataframe(imp)

                # ==========================================
                # AI Decision Report
                # ==========================================

                decision_engine = DecisionEngine()

                research_report = st.session_state.get(
                    "research_report",
                    "No research report available."
                )

                decision_report = decision_engine.generate(
                    research_report,
                    best_model,
                    problem_type
                )

                st.divider()
                st.header("🧠 AI Decision Report")
                st.write(decision_report)

                st.divider()
                

            except Exception as e:
                st.error(f"Error: {e}")
            # =====================================================
# Prediction Section
# =====================================================

    if st.session_state.get("model_trained", False):

        st.divider()

        st.header("🔮 Predict on New Data")

        user_input = {}

        for col in st.session_state["feature_columns"]:

            user_input[col] = st.number_input(
                col,
                value=0.0,
                key=col
            )

        input_df = pd.DataFrame([user_input])

        if st.button("Predict"):

            input_encoded = pd.get_dummies(input_df)

            if hasattr(st.session_state["trained_model"], "feature_names_in_"):

                input_encoded = input_encoded.reindex(
                    columns=st.session_state["trained_model"].feature_names_in_,
                    fill_value=0
                )

            prediction = st.session_state["trained_model"].predict(
                input_encoded
            )

            st.success(f"🎯 Prediction : {prediction[0]}")