class ExecutiveSummary:
    
    def generate(self, best_model, problem_type):

        summary = {}

        summary["Problem Type"] = problem_type

        summary["Best Model"] = best_model["Model"]

        if problem_type == "Classification":

            summary["Score"] = f"Accuracy : {best_model['Accuracy']:.4f}"

        else:

            summary["Score"] = f"R² Score : {best_model['R2 Score']:.4f}"

        # Top Features
        features = []

        if best_model.get("Feature Importance"):

            sorted_features = sorted(
                best_model["Feature Importance"].items(),
                key=lambda x: x[1],
                reverse=True
            )

            features = [x[0] for x in sorted_features[:5]]

        summary["Top Features"] = features

        summary["Recommendation"] = (
            f"{best_model['Model']} is recommended because "
            f"it achieved the best performance on the uploaded dataset."
        )

        return summary