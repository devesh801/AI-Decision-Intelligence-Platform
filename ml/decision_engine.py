class DecisionEngine:
    
    def decide(self, profile, quality):

        decisions = []

        # Missing Values
        total_missing = sum(
            quality["missing_values"].values()
        )

        if total_missing > 0:

            decisions.append(
                "Handle missing values before training."
            )

        # Duplicate Rows
        if quality["duplicate_rows"] > 0:

            decisions.append(
                "Remove duplicate rows."
            )

        # Outliers
        total_outliers = sum(
            quality["outliers"].values()
        )

        if total_outliers > 0:

            decisions.append(
                "Check numerical outliers."
            )

        # Numerical Features
        if len(quality["numerical_columns"]) > 5:

            decisions.append(
                "Feature scaling is recommended."
            )

        # Categorical Features
        if len(quality["categorical_columns"]) > 0:

            decisions.append(
                "Categorical encoding is required."
            )

        return decisions