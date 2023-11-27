import tkinter as tk
from tkinter import filedialog
from image_manipulator import image_manipulator

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing GUI")
        self.root.geometry("400x400")

        self.create_button("Select Image", self.select_image, "blue", "white", pady=20, font_size=14)
        self.create_button("Close Window", self.close_window, "red", "white", pady=20, font_size=14)

    def create_button(self, text, command, bg, fg, **kwargs):
        font_size = kwargs.pop("font_size", 12)  # Remove font_size from kwargs
        button = tk.Button(self.root, text=text, command=command, background=bg, foreground=fg, font=("Helvetica", font_size))
        button.pack(**kwargs)

    def select_image(self):
        path = filedialog.askopenfilename()
        image_manipulator.process_image(path)

    def close_window(self):
        self.root.destroy()
