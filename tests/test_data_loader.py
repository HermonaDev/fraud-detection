from src.data_loader import validate_data
import pandas as pd

def test_validate_data():
    df = pd.DataFrame({"A": [1], "B": [2]})
    assert validate_data(df, ["A", "B"]) == True
    assert validate_data(df, ["A", "C"]) == False