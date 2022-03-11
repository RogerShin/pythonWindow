import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #上方的Frame=========start
        topFrame = tk.Frame(self,background='red')
        tk.Label(topFrame,text="台北市youbike即時監測系統",font=("arial",20)).pack()
        topFrame.grid(column=0,row=0,columnspan=3,padx=20,pady=20)
        #上方的Frame=========end
        LeftLabelFrame(self,background='blue',text="左邊的").grid(column=0,row=1,padx=20,pady=20)



        centerBottom = tk.LabelFrame(self,background='gray',text="中間的")
        tk.Label(centerBottom, text="將無車可借站點", font=("arial", 20)).pack()
        centerBottom.grid(column=1,row=1,padx=20,pady=20)

        rightBottom = tk.LabelFrame(self, background='green',text="右邊的")
        tk.Label(rightBottom, text="將無法還車站點", font=("arial", 20)).pack()
        rightBottom.grid(column=2, row=1, padx=20, pady=20)

class LeftLabelFrame(tk.LabelFrame):
    def __init__(self, *args , **kwargs):
        super().__init__(*args, **kwargs)
        tk.Label(self, text="正常租借站點", font=("arial", 20)).pack()

if __name__=="__main__":
    dataSource.update_youbike_data()
    window = Window()
    window.title("台北市youbike及時監測資料")
    window.mainloop()
