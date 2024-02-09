import numpy as np


def ft_invert(array) -> np.ndarray:
    """Invert the colors of the image."""
    return 255 - array

def ft_red(array) -> np.ndarray:
    """Get the red channel of the image."""
    array[:, :, 1] = 0  # Mettre à zéro le canal vert
    array[:, :, 2] = 0  # Mettre à zéro le canal bleu
    return array

def ft_blue(array) -> np.ndarray:
    """Get the blue channel of the image."""
    array[:, :, 0] = 0  # Mettre à zéro le canal rouge
    array[:, :, 1] = 0  # Mettre à zéro le canal vert
    return array

def ft_green(array) -> np.ndarray:
    """"Get the green channel of the image."""
    array[:, :, 0] = 0  # Mettre à zéro le canal rouge
    array[:, :, 2] = 0  # Mettre à zéro le canal bleu
    return array

def ft_grey(array) -> np.ndarray:
    """Convert the image to greyscale."""
    grey_array = array.mean(axis=2, keepdims=True).astype(array.dtype)
    return np.concatenate([grey_array] * 3, axis=2)