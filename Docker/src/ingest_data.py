from sklearn.datasets import fetch_california_housing
import pandas as pd
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def ingest_data():
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    os.makedirs("../data", exist_ok=True)
    df.to_csv("../data/housing.csv", index=False)

if __name__ == "__main__":
    ingest_data()