import os
import pickle
import json
from datetime import datetime

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def save_model(model, directory="models/"):
    ensure_dir(directory)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"model_{timestamp}.pkl")
    with open(filename, "wb") as f:
        pickle.dump(model, f)
    return filename

def load_latest_model(directory="models/"):
    ensure_dir(directory)
    files = [f for f in os.listdir(directory) if f.endswith(".pkl")]
    if not files:
        raise FileNotFoundError("No saved model found.")
    latest = max(files)
    with open(os.path.join(directory, latest), "rb") as f:
        model = pickle.load(f)
    return model, latest

def save_metrics(metrics, directory="metrics/"):
    ensure_dir(directory)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"metrics_{timestamp}.json")
    with open(filename, "w") as f:
        json.dump(metrics, f, indent=4)
    return filename
