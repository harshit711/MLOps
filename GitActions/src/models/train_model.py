from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from src.features.generate_data import generate_air_quality_data
from src.models.model_utils import save_model

def train_model():
    df = generate_air_quality_data()

    X = df.drop("risk", axis=1)
    y = df["risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    path = save_model(model)
    print(f"Model saved to {path}")

if __name__ == "__main__":
    train_model()
