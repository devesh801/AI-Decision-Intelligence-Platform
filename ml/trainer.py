from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class ModelTrainer:

    def train(
        self,
        model,
        X,
        y
    ):

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model.fit(X_train, y_train)

        prediction = model.predict(X_test)

        score = accuracy_score(
            y_test,
            prediction
        )

        return {
            "model": model,
            "accuracy": score
        }