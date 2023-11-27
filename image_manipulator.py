import cv2
import numpy as np
class image_manipulator:
    def process_image(path):
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=3)
        clahe_image = clahe.apply(gray)
        blurred = cv2.GaussianBlur(clahe_image, (9, 9), 0)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        high_pass = cv2.filter2D(blurred, -1, kernel)
        alpha = 1.2
        beta = 40
        adjusted = cv2.convertScaleAbs(high_pass, alpha=alpha, beta=beta)
        kernel_morph = np.ones((2, 2), np.uint8)
        morph = cv2.morphologyEx(adjusted, cv2.MORPH_OPEN, kernel_morph)
        inverted = cv2.bitwise_not(morph)
        cv2.imshow('X-ray-like Image', inverted)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
