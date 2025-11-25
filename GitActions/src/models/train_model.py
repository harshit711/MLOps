import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.features.generate_data import generate_air_quality_data
from src.models.model_utils import save_model

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train():
    df = generate_air_quality_data()

    X = df.drop("risk", axis=1)
    y = df["risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    save_model(model)
    print("Model training complete.")

if __name__ == "__main__":
    train()
