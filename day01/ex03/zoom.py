from load_image import ft_load
from matplotlib import pyplot as plt


def zoom_image(image_array, zoom_factor):
    """Zoom the image."""
    center_x, center_y = image_array.shape[1] // 2, image_array.shape[0] // 2

    new_width = int(image_array.shape[1] / zoom_factor)
    new_height = int(image_array.shape[0] / zoom_factor)

    zoomed_image = image_array[
        center_y - new_height // 2:center_y + new_height // 2,
        center_x - new_width // 2:center_x + new_width // 2]
    return zoomed_image


def main():
    """Main function."""
    data = ft_load("animal.jpeg")
    print(f"The shape of the image is: {data.shape}")
    data = zoom_image(data, 2)
    print("The shape after slicing:"
          f" {data.shape} or ({data.shape[0]}, {data.shape[1]})")

    plt.imshow(data)
    plt.show()


if __name__ == "__main__":
    main()
