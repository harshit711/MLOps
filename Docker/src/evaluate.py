import joblib
from sklearn.metrics import mean_squared_error, r2_score
from preprocess import preprocess_data

def evaluate_model():
    X_train, X_test, y_train, y_test = preprocess_data()
    model = joblib.load("../model/model.pkl")

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Model Evaluation:")
    print(f"MSE = {mse:.3f}")
    print(f"R2  = {r2:.3f}")

if __name__ == "__main__":
    evaluate_model()