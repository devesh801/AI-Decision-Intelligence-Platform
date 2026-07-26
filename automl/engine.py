import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

# Classification Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Regression Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class AutoMLEngine:

    def detect_problem(self, y):

        if y.dtype == "object":
            return "Classification"

        if y.nunique() <= 20:
            return "Classification"

        return "Regression"

    def get_models(self, problem_type):

        if problem_type == "Classification":

            return {
                "Logistic Regression": LogisticRegression(max_iter=1000),
                "Decision Tree": DecisionTreeClassifier(random_state=42),
                "Random Forest": RandomForestClassifier(random_state=42)
            }

        return {
            "Linear Regression": LinearRegression(),
            "Decision Tree": DecisionTreeRegressor(random_state=42),
            "Random Forest": RandomForestRegressor(random_state=42)
        }

    def train(self, X, y):

        problem_type = self.detect_problem(y)

        # Encode categorical features
        X = pd.get_dummies(X)

        # Encode target if classification
        if problem_type == "Classification" and y.dtype == "object":
            y = pd.factorize(y)[0]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        leaderboard = []

        best_model = None
        best_score = float("-inf")

        for name, model in self.get_models(problem_type).items():

            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            # -------------------------
            # Feature Importance
            # -------------------------

            feature_importance = None

            if hasattr(model, "feature_importances_"):

                feature_importance = dict(
                    zip(
                        X.columns,
                        np.round(model.feature_importances_, 4)
                    )
                )

            elif hasattr(model, "coef_"):

                coef = model.coef_

                if len(np.array(coef).shape) > 1:
                    coef = coef[0]

                feature_importance = dict(
                    zip(
                        X.columns,
                        np.round(np.abs(coef), 4)
                    )
                )

            # =========================
            # Classification
            # =========================

            if problem_type == "Classification":

                accuracy = accuracy_score(y_test, y_pred)

                precision = precision_score(
                    y_test,
                    y_pred,
                    average="weighted",
                    zero_division=0
                )

                recall = recall_score(
                    y_test,
                    y_pred,
                    average="weighted",
                    zero_division=0
                )

                f1 = f1_score(
                    y_test,
                    y_pred,
                    average="weighted",
                    zero_division=0
                )

                cm = confusion_matrix(
                    y_test,
                    y_pred
                )

                leaderboard.append({

                    "Model": name,
                    "Accuracy": round(accuracy, 4),
                    "Precision": round(precision, 4),
                    "Recall": round(recall, 4),
                    "F1 Score": round(f1, 4),
                    "Confusion Matrix": cm.tolist(),
                    "Feature Importance": feature_importance

                })

                if accuracy > best_score:

                    best_score = accuracy
                    best_model = model

            # =========================
            # Regression
            # =========================

            else:

                r2 = r2_score(
                    y_test,
                    y_pred
                )

                mae = mean_absolute_error(
                    y_test,
                    y_pred
                )

                rmse = np.sqrt(
                    mean_squared_error(
                        y_test,
                        y_pred
                    )
                )

                leaderboard.append({

                    "Model": name,
                    "R2 Score": round(r2, 4),
                    "MAE": round(mae, 4),
                    "RMSE": round(rmse, 4),
                    "Feature Importance": feature_importance

                })

                if r2 > best_score:

                    best_score = r2
                    best_model = model

        # =========================
        # Sort Leaderboard
        # =========================

        if problem_type == "Classification":

            leaderboard.sort(
                key=lambda x: x["Accuracy"],
                reverse=True
            )

        else:

            leaderboard.sort(
                key=lambda x: x["R2 Score"],
                reverse=True
            )

        return leaderboard, problem_type, best_model