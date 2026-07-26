import pandas as pd


class DataQualityAnalyzer:

    def analyze(self, df):

        report = {}

        # Missing Values
        report["missing_values"] = df.isnull().sum().to_dict()

        # Duplicate Rows
        report["duplicate_rows"] = int(df.duplicated().sum())

        # Data Types
        report["data_types"] = df.dtypes.astype(str).to_dict()

        # Numerical Columns
        report["numerical_columns"] = list(
            df.select_dtypes(include=["number"]).columns
        )

        # Categorical Columns
        report["categorical_columns"] = list(
            df.select_dtypes(include=["object", "category"]).columns
        )

        # Outliers (IQR Method)
        outliers = {}

        numeric_df = df.select_dtypes(include=["number"])

        for column in numeric_df.columns:

            Q1 = numeric_df[column].quantile(0.25)
            Q3 = numeric_df[column].quantile(0.75)

            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            count = ((numeric_df[column] < lower) |
                     (numeric_df[column] > upper)).sum()

            outliers[column] = int(count)

        report["outliers"] = outliers

        return report