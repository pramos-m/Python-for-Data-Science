import cv2  # OpenCV, una librería para el procesamiento de imágenes.

def ft_load(path: str):
    try:
        # load the image in BGR format (default OpenCV format color)
        image_bgr = cv2.imread(path)
        # Convert the image from BGR to RGB (more standard)
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        # print the image shape (width, height, and color chanels)
        print(image_rgb.shape)
        # Return the loaded image
        return image_rgb
    except Exception as err:
        print("Error:", err)
        return None

