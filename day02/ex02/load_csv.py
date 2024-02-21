import pandas as pd


def convert_units(value):
    """Convert the string number with units to a number."""
    if isinstance(value, str):
        if 'B' in value:
            return float(value.replace('B', '')) * 1e9
        elif 'M' in value:
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
    try:
        return float(value)
    except ValueError:
        return None


def load(path: str) -> pd.DataFrame or None:
    """Load a csv file into a pandas DataFrame."""
    try:
        converters = {str(year): convert_units for year in range(1800, 2200)}
        data = pd.read_csv(path, converters=converters)
        print(f"Loading dataset of shape {data.shape}")
        return data
    except Exception as e:
        print(f"error load csv: {e}")
        return None
