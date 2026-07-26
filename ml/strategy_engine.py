import pandas as pd


class StrategyEngine:

    def recommend(self, profile, quality, target, df):

        target_dtype = df[target].dtype
        unique_values = df[target].nunique()

        # -----------------------------
        # Detect Problem Type
        # -----------------------------

        if (
            target_dtype == "object"
            or str(target_dtype) == "category"
            or unique_values <= 10
        ):
            problem_type = "Classification"

            models = [
                "Logistic Regression",
                "Decision Tree",
                "Random Forest"
            ]

            metric = "Accuracy"

        else:

            problem_type = "Regression"

            models = [
                "Linear Regression",
                "Decision Tree Regressor",
                "Random Forest Regressor"
            ]

            metric = "R² Score"

        # -----------------------------
        # Cleaning Suggestions
        # -----------------------------

        cleaning = []

        if sum(profile["missing_values"].values()) > 0:
            cleaning.append("Fill Missing Values")

        if quality["duplicate_rows"] > 0:
            cleaning.append("Remove Duplicate Rows")

        if len(quality["outliers"]) > 0:
            cleaning.append("Handle Outliers")

        if not cleaning:
            cleaning.append("Dataset looks clean")

        return {
            "problem_type": problem_type,
            "metric": metric,
            "models": models,
            "cleaning": cleaning
        }