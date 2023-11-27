import tkinter as tk
from GUI import GUI


class MainApp:


    def __init__(self):
        self.root = tk.Tk()
        self.gui = GUI(self.root)
        self.root.mainloop()

if __name__ == "__main__":
    app = MainApp()
