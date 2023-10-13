import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Users\Ayad\OneDrive\Desktop\computer_graphics\teeth.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply bilateral filter to reduce noise while maintaining edges
bilateral_filtered = cv2.bilateralFilter(gray, 9, 75, 75)

# Invert the image for a more realistic X-ray appearance
inverted = cv2.bitwise_not(bilateral_filtered)

# Display the resulting X-ray-like image
cv2.imshow('X-ray-like Image', inverted)
cv2.waitKey(0)
cv2.destroyAllWindows()
