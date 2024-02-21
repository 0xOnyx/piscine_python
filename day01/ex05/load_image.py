from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load the image from a file."""
    img = Image.open(path)
    img.load()
    data = np.asarray(img, dtype="int32")
    print(f"The shape of image is: {data.shape}")
    print(data)
    return data
