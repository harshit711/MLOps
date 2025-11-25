import pandas as pd
from sklearn.datasets import make_classification

def generate_air_quality_data(n_samples=1000, random_state=42):
    """
    Generates synthetic air quality data with 8 features and a binary label 'risk'.
    """
    X, y = make_classification(
        n_samples=n_samples,
        n_features=8,
        n_informative=5,
        n_redundant=1,
        random_state=random_state
    )

    df = pd.DataFrame(
        X,
        columns=["PM25","PM10","NO2","SO2","CO","TEMP","HUMIDITY","WIND"]
    )
    
    df["risk"] = y
    return df