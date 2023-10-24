import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\Anton\OneDrive\Desktop\teeth_2.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive histogram equalization to enhance contrast
#enhance contrast on grayscale image.
## contrast limit adaptive histogram equalizer
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(gray)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(clahe_image, (9, 9), 0)

# high-pass filter to enhance edges
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
high_pass = cv2.filter2D(blurred, -1, kernel)

# contrast and brightness to enhance details
# between 1.2 to 1.8 would be good for aplha
alpha = 1.2  # Contrast control (1.0-3.0)
beta = 40  # Brightness control (0-100)
adjusted = cv2.convertScaleAbs(high_pass, alpha=alpha, beta=beta)

# Apply morphological transformations for noise reduction
kernel = np.ones((2, 2), np.uint8)
#to remove small bright spots and dark spots from the image.
morph = cv2.morphologyEx(adjusted, cv2.MORPH_OPEN, kernel)

# Invert the image for a more realistic X-ray appearance
#to create a "negative" version of the original image
inverted = cv2.bitwise_not(morph)

# Display the resulting X-ray-like image
cv2.imshow('X-ray-like Image', inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
