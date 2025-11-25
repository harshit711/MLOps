import unittest
from src.features.generate_data import generate_air_quality_data

class TestAirQuality(unittest.TestCase):

    def test_columns(self):
        df = generate_air_quality_data()
        self.assertEqual(len(df.columns), 9)

    def test_no_nulls(self):
        df = generate_air_quality_data()
        self.assertFalse(df.isnull().any().any())

if __name__ == "__main__":
    unittest.main()