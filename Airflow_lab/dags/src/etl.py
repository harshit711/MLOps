import pandas as pd
import os, pickle, base64

def extract_data():
    """Load cryptocurrency data from local CSV."""
    data_path = os.path.join(os.path.dirname(__file__), "../data/crypto_raw.csv")
    df = pd.read_csv(data_path)

    serialized = pickle.dumps(df)
    return base64.b64encode(serialized).decode("ascii")


def transform_data(data_b64):
    """Clean and normalize price data."""
    df = pickle.loads(base64.b64decode(data_b64))
    df["priceUsd"] = df["priceUsd"].round(2)
    df.rename(columns={"priceUsd": "price_usd"}, inplace=True)

    serialized = pickle.dumps(df)
    return base64.b64encode(serialized).decode("ascii")


def load_data(data_b64):
    """Store transformed data to a CSV file."""
    df = pickle.loads(base64.b64decode(data_b64))
    output_path = os.path.join(os.path.dirname(__file__), "../data/crypto_clean.csv")
    df.to_csv(output_path, index=False)
    return output_path


def analyze_data(file_path):
    """Compute average price per symbol and overwrite the CSV with averages."""
    df = pd.read_csv(file_path)

    avg_df = (
        df.groupby(["id", "symbol"], as_index=False)["price_usd"]
        .mean()
        .round(2)
    )

    avg_df.to_csv(file_path, index=False)

    return file_path