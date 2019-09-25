import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageFilter

class Main:
    def __init__(self):
        self.txt = tk.Entry(width=300)
        self.frame1
        self.frame2
        self.chooseExtension
        self.root = tk.Tk()

    def main(self):
        self.root.title("Tkinter test")
        self.root.geometry("450x100")
        self.root.mainloop()

    def initFrame1(self):
        button = tk.Button(self.root,text="変換")



if __name__=="__main__":
