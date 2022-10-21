import tkinter as tk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        mainCanvas = tk.Canvas(self,width=640,height=427)
        bgImage = Image.open('bg.jpg')
        tkImage = ImageTk.PhotoImage(bgImage)
        mainCanvas.create_image(0,0,anchor=tk.NW,image=tkImage)
        mainCanvas.pack()


def main():
    window = Window()
    window.title("Frame框架")
    window.geometry("640x427")
    window.mainloop()

if __name__ == "__main__":
    main()