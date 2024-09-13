from load_image import ft_load
import matplotlib.pyplot as plt

def cut_square(image):
    # Recorta un área cuadrada de 400x400 píxeles.
    return image[100:500, 100:500]  # Ajusta los valores según sea necesario

def transpose_image(image):
    # Transponer manualmente la matriz de la imagen (intercambiar filas y columnas).
    transposed_image = [[image[j][i] for j in range(len(image))] for i in range(len(image[0]))]
    return transposed_image

def display_image(image, title="Image"):
    try:
        plt.imshow(image)
        plt.title(title)
        plt.show()
    except Exception as err:
        print(f"Error showing the image: {err}")

def main():
    image_path = "animal.jpeg"
    image = ft_load(image_path)

    if image is None:
        print("Error loading the image.")
        return

    # Recortar un cuadrado de la imagen
    square_image = cut_square(image)
    print(f"The shape of the square image is: {square_image.shape}")
    print(square_image)

    # Transponer la imagen
    transposed_image = transpose_image(square_image)
    print(f"New shape after Transpose: ({len(transposed_image)}, {len(transposed_image[0])})")
    print(transposed_image)

    # Mostrar la imagen recortada y transpuesta
    display_image(square_image, "Original Square Image")
    display_image(transposed_image, "Transposed Image")

if __name__ == "__main__":
    main()

