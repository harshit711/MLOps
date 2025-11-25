import os
import pickle
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MODELS_DIR = os.path.join(BASE_DIR, "models")
METRICS_DIR = os.path.join(BASE_DIR, "metrics")

os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(METRICS_DIR, exist_ok=True)


def save_model(model):
    """Save model with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(MODELS_DIR, f"model_{timestamp}.pkl")

    with open(path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to: {path}")
    return path


def load_latest_model():
    """Load the most recent model file from GitActions/models"""
    files = [f for f in os.listdir(MODELS_DIR) if f.endswith(".pkl")]

    if not files:
        raise FileNotFoundError("No model .pkl files found in models directory.")

    # Get newest model file by timestamp
    latest = sorted(files)[-1]
    path = os.path.join(MODELS_DIR, latest)

    with open(path, "rb") as f:
        model = pickle.load(f)

    print(f"Loaded latest model: {latest}")
    return model, latest


def save_metrics(metrics_dict):
    """Save metrics json file"""
    import json

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(METRICS_DIR, f"metrics_{timestamp}.json")

    with open(path, "w") as f:
        json.dump(metrics_dict, f, indent=4)

    print(f"Metrics saved to: {path}")
    return path
