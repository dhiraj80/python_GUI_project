from tkinter import *


class Gui:
    def __init__(self,root):
        self.root = root



        self.root.r = PhotoImage(file="D:\\all icons\\file.png")

        Label(self,image=self.root.r).pack()
        
root=Tk()
obj = Gui(root)
root.mainloop()
# root.mainloop()