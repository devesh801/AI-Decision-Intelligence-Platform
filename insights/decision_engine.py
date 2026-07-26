class DecisionEngine:
    
    def generate(
        self,
        research_report,
        best_model,
        problem_type
    ):

        report = f"""
# 🧠 AI Decision Report

## 📄 Research Insights

{research_report[:1200]}

--------------------------------------------------

## 🤖 Machine Learning Insights

Best Model:
{best_model['Model']}

Problem Type:
{problem_type}

"""

        if problem_type == "Classification":

            report += f"""
Accuracy:
{best_model['Accuracy']}

Precision:
{best_model['Precision']}

Recall:
{best_model['Recall']}

F1 Score:
{best_model['F1 Score']}
"""

        else:

            report += f"""
R² Score:
{best_model['R2 Score']}

MAE:
{best_model['MAE']}

RMSE:
{best_model['RMSE']}
"""

        report += """

--------------------------------------------------

## 💡 AI Decision

The machine learning model has identified the best predictive approach based on the uploaded dataset.

The research report provides additional background and context that helps explain the prediction.

Together, these provide a more informed decision than using research or machine learning alone.
"""

        return report