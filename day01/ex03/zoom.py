from load_image import ft_load
from matplotlib import pyplot as plt

def zoom_image(image_array, zoom_factor):
    # Déterminer le centre de l'image
    center_x, center_y = image_array.shape[1] // 2, image_array.shape[0] // 2

    # Calculer les dimensions de la nouvelle image après le zoom
    new_width = int(image_array.shape[1] / zoom_factor)
    new_height = int(image_array.shape[0] / zoom_factor)

    # Extraire la portion de l'image
    zoomed_image = image_array[center_y - new_height // 2:center_y + new_height // 2,
                   center_x - new_width // 2:center_x + new_width // 2]
    return zoomed_image


def main():
    data = ft_load("animal.jpeg")
    print(f"The shape of the image is: {data.shape}")
    data = zoom_image(data, 2)
    print(f"The shape after slicing: {data.shape} or ({data.shape[0]}, {data.shape[1]})")

    plt.imshow(data)
    plt.show()


if __name__ == "__main__":
    main()
