from tkinter import *
from PIL import Image,ImageTk,ImageDraw

root = Tk()

root.geometry("1400x1000+0+0")
root.title("new windows")

def clock_img():
    clock = Image.new("RGB",(40,40),(255,0,255)) 



# img = Image.open("D:\\all icons\\20211221_084828.jpg")
# img = img.resize((500,500),Image.ANTIALIAS)
# pic = ImageTk.PhotoImage(image=img)

la = Label(root,text="Anloge Clock",bg="gray",bd=15,relief=GROOVE,font=("arial 80 bold"))
la.pack(anchor=CENTER,pady=30,fill=X)

la_pic = Label(root,bg="yellow",bd=15,relief=GROOVE,width=70,height=30)
la_pic.pack()



clock_img()
root.mainloop()