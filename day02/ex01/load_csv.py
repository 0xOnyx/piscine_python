import pandas as pd


def load(path: str) -> pd.DataFrame or None:
    try:
        data = pd.read_csv(path)
        print(f"Loading dataset of shape {data.shape}")
        return data
    except Exception as e:
        print(f"error load csv: {e}")
        return None
