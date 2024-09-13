import cv2 as cv2


def ft_load(path: str):
    try:
        # path to input image is specified and image is loaded with imread command
        image_bgr = cv2.imread(path) # reading img, sintax: 1.path,2.flag
        # to convert the image in rgb
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        print(image_rgb.shape)
        return (image_rgb)
    except Exception as err:
        print("Error:", err)
