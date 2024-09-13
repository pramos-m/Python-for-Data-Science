from load_image import ft_load
import cv2
import matplotlib.pyplot as plt

def zoom_image(image):
    # Adjust the coordinates as needed
    zoomed_image = image[100:500, 200:600] 
    print(f"New shape after slicing: {zoomed_image.shape}")
    return zoomed_image

def display_image(image, title="Image"):
    try:
        # Show image using matplotlib
        plt.imshow(image)
        plt.title(title)
        plt.xlabel("X-axis")  # Staired X axis
        plt.ylabel("Y-axis")  # Staired Y axis
        plt.show()
    except Exception as err:
        print(f"Error showing the image: {err}")

def main():
    # Load the image
    image_path = "animal.jpeg"
    image = ft_load(image_path)

    if image is None:
        print("Error loading the image.")
        return

    # Show image info
    print("The shape of the image is:", image.shape)
    print(image)

    # Zoom into the image
    zoomed_image = zoom_image(image)
    
    # Show both images: original and zoomed
    display_image(image, "Original Image")
    display_image(zoomed_image, "Zoomed Image")

if __name__ == "__main__":
    main()
