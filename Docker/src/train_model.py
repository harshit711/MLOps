import joblib
from sklearn.linear_model import LinearRegression
from preprocess import preprocess_data
import os

def train_model():
    X_train, X_test, y_train, y_test = preprocess_data()

    model = LinearRegression()
    model.fit(X_train, y_train)

    os.makedirs("../model", exist_ok=True)
    joblib.dump(model, "../model/model.pkl")
    print("Model trained and saved!")

if __name__ == "__main__":
    train_model()