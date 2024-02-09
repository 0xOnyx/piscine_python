import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def cut_and_transpose(image_array):
    cute_image = cut_square(image_array)
    return manual_transpose(cute_image)

def cut_square(image_array):
    size = min(image_array.shape[:2])
    square_image = image_array[:size, :size]
    return square_image


def manual_transpose(image_array):
    transposed_image = np.zeros((image_array.shape[1], image_array.shape[0], image_array.shape[2]),
                                dtype=image_array.dtype)

    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            transposed_image[j, i] = image_array[i, j]

    return transposed_image


def main():
    image_path = "animal.jpeg"
    image_array = ft_load(image_path)

    print(f"The shape of the image is: {image_array.shape} or ({image_array.shape[0]}, {image_array.shape[1]})")

    transposed_image = cut_and_transpose(image_array)

    plt.imshow(transposed_image)
    plt.show()

    print(f"New shape after Transpose: ({transposed_image.shape[0]}, {transposed_image.shape[1]})")
    print(transposed_image)


if __name__ == "__main__":
    main()
