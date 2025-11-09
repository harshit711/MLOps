from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="House Price Prediction API",
              description="Predict house prices using a trained Linear Regression model",)

model = joblib.load("../model/model.pkl")
scaler = joblib.load("../model/scaler.pkl")

class HouseFeatures(BaseModel):
    features: list[float]

@app.get("/")
def root():
    return {"message": "House Price Prediction API is running!"}

@app.post("/predict")
def predict(data: HouseFeatures):
    features = np.array(data.features).reshape(1, -1)
    scaled = scaler.transform(features)
    prediction = float(model.predict(scaled)[0])
    return {"predicted_price": prediction}