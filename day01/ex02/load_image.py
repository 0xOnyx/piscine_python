from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        img = Image.open(path)
        img.load()
        data = np.asarray(img, dtype="int32")
        return data
    except Exception as e:
        print(f"error load image: {e}")
        exit()
