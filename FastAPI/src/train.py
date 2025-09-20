from sklearn.tree import DecisionTreeClassifier
import joblib
from data import load_data, split_data, scale_data

def fit_model(X_train, y_train):
    """
    Train a Decision Tree Classifier and save the model to a file.
    Args:
        X_train (numpy.ndarray): Training features.
        y_train (numpy.ndarray): Training target values.
    """
    dt_classifier = DecisionTreeClassifier(max_depth=3, random_state=12)
    dt_classifier.fit(X_train, y_train)
    joblib.dump(dt_classifier, "../model/iris_model.pkl")

if __name__ == "__main__":
    X, y = load_data()
    X_train, X_test, y_train, y_test = split_data(X, y)
    X_train, X_test, scaler = scale_data(X_train, X_test)
    joblib.dump(scaler, "../model/scaler.pkl")
    fit_model(X_train, y_train)
