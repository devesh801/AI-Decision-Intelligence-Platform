class InsightGenerator:
    
    def generate(
        self,
        strategy,
        leaderboard,
        profile,
        quality
    ):

        best_model = leaderboard[0]

        report = f"""
==============================
EXECUTIVE SUMMARY
==============================

Problem Type:
{strategy["problem_type"]}

Rows:
{profile["rows"]}

Columns:
{profile["columns"]}

--------------------------------

Best Model

{best_model["Model"]}

Accuracy

{best_model["Accuracy"]}

--------------------------------

Dataset Quality

Duplicate Rows :
{quality["duplicate_rows"]}

--------------------------------

Recommended Cleaning
"""

        for item in strategy["cleaning"]:

            report += f"\n✔ {item}"

        report += """

--------------------------------

Recommended Models
"""

        for model in strategy["models"]:

            report += f"\n• {model}"

        report += """

--------------------------------

Business Insight

The selected model achieved the highest
performance on the uploaded dataset.

The dataset should continue to be monitored
for quality, missing values and outliers.

The model should be validated before
deployment into production.

==============================
"""

        return report