import numpy as np
import matplotlib.pyplot as plt
import os


def generate_spray_matrix(size: int, n_colors: int):
    b = np.random.randint(0, n_colors, size=(size, size // 2 + size % 2))
    if size % 2 == 1:
        return np.pad(b, [(0, 0), (0, size // 2)], "reflect")
    return np.pad(b, [(0, 0), (0, size // 2)], "symmetric")


def generate_and_save_spray(path: str, size: int, n_colors: int):
    plt.imsave(path, generate_spray_matrix(size, n_colors))


def user_interface():
    print("Enter the number of sprays to create:")
    n_sprays = input()
    while type(n_sprays) != int:
        try:
            n_sprays = int(n_sprays)
        except ValueError:
            print("Error! It must be int number of sprays you want to create! Input again: ")
            n_sprays = input()
    print("Enter the size of sprays:")
    sprays_size = input()
    while type(sprays_size) != int:
        try:
            sprays_size = int(sprays_size)
        except ValueError:
            print("Error! It must be int size of sprays! Input again: ")
            sprays_size = input()
    print("Enter the number of colors to paint sprays:")
    n_colors = input()
    while type(n_colors) != int:
        try:
            n_colors = int(n_colors)
        except ValueError:
            print("Error! It must be int number of colors you want to paint! Input again: ")
            n_colors = input()
    print("Enter the path to the folder where to upload:")
    folder_path = input()
    while not os.path.exists(folder_path):
        print("Error! Directory does not exist ")
        folder_path = input()
    for n in range(0, n_sprays):
        generate_and_save_spray(folder_path + f"/spray_{n}.png", sprays_size, n_colors)
    print(f"{n_sprays} sprays created successfully")


user_interface()
