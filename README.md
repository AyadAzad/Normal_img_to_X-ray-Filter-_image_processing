# Image Processing GUI

This Python project provides a simple graphical user interface (GUI) for processing and enhancing images, it converts normal image to grayscale like image which is similar to an X-ray filter image. The project is divided into three main files:

1. **MainApp.py**: Initializes the tkinter application and launches the GUI.
2. **image_manipulator.py**: Contains a class for processing images using OpenCV.
3. **GUI.py**: Implements the GUI using tkinter and allows users to select an image for processing.

## Getting Started

### Prerequisites

- Ensure you have Python installed on your system.
- Install the required libraries using the following command:

   ```bash
   pip install opencv-python numpy
   ```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AyadAzad/image-processing-gui.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-processing-gui
   ```

3. Run the `MainApp.py` file:

   ```bash
   python MainApp.py
   ```

## Features

- **Select Image**: Opens a file dialog to choose an image for processing.
- **Image Processing**: Applies a series of image processing techniques, including grayscale conversion, contrast adjustment, and morphological operations.
- **Display Result**: Displays the processed image in a new window.
- **Close Window**: Closes the application window.

## Usage

1. Run the `MainApp.py` file.
2. Click the "Select Image" button to choose an image from your file system.
3. The processed image will be displayed in a new window with X-ray-like enhancements.
4. Close the application window using the "Close Window" button.

## Contributing

Feel free to contribute to the project by submitting pull requests or reporting issues.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the OpenCV library for providing powerful image processing capabilities.
- The tkinter library for creating the graphical user interface.

---

