from src.features.generate_data import generate_air_quality_data

def test_data_shape():
    df = generate_air_quality_data()
    assert df.shape == (1000, 9)

def test_risk_values():
    df = generate_air_quality_data()
    assert set(df["risk"].unique()) == {0, 1}