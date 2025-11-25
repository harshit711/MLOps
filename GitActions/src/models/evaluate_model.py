import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.features.generate_data import generate_air_quality_data
from src.models.model_utils import load_latest_model, save_metrics

from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

def evaluate():
    df = generate_air_quality_data()

    X = df.drop("risk", axis=1)
    y = df["risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model, model_name = load_latest_model()

    preds = model.predict(X_test)

    metrics = {
        "model": model_name,
        "accuracy": accuracy_score(y_test, preds),
        "f1_score": f1_score(y_test, preds)
    }

    save_metrics(metrics)
    print("Evaluation complete.")

if __name__ == "__main__":
    evaluate()
