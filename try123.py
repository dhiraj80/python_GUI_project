import urllib.request
from PIL import ImageTk,Image
from tkinter import *

root = Tk()
root.geometry("1400x1000+0+0")
root.title('YouTube Video Donwloder')
root.config(bg="#ff0077")

urllib.request.urlretrieve("https://i.ytimg.com/vi/1Wz0AwQi9Ow/sddefault.jpg","th_img.png")

#img_path = img_path.resize((950,600),Image.ANTIALIAS)
img = PhotoImage(file='th_img.png')



th_img = Label(root,bd=0,image=img)
th_img.pack()

root.mainloop()