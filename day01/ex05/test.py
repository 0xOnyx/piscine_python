from matplotlib import pyplot as plt

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

def set_function_name(func, array):
    plt.imshow(func(array))
    plt.show()


def main():
    image_path = "landscape.jpg"
    array = ft_load(image_path)

    set_function_name(ft_invert, array.copy())
    set_function_name(ft_red, array.copy())
    set_function_name(ft_green, array.copy())
    set_function_name(ft_blue, array.copy())
    set_function_name(ft_grey, array.copy())

    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
