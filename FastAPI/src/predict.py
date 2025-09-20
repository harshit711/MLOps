import joblib

def predict_data(X):
    """
    Predict the class labels for the input data.
    Args:
        X (numpy.ndarray): Input data for which predictions are to be made.
    Returns:
        y_pred (numpy.ndarray): Predicted class labels.
    """
    scaler = joblib.load("../model/scaler.pkl")
    X_scaled = scaler.transform(X)
    model = joblib.load("../model/iris_model.pkl")
    y_pred = model.predict(X_scaled)
    return y_pred
