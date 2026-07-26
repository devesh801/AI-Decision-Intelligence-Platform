import pandas as pd


class ProblemDetector:

    def detect(self, df, target_column=None):

        # No target column → Clustering
        if target_column is None:
            return "Clustering"

        target = df[target_column]

        # Text or category → Classification
        if target.dtype == "object":
            return "Classification"

        unique_values = target.nunique()

        # Numeric with few unique values → Classification
        if unique_values <= 10:
            return "Classification"

        # Numeric with many values → Regression
        return "Regression"