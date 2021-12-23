from tkinter import *
from tkinter import ttk,messagebox,filedialog
import time,os

root = Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}+0+0")
root.wm_iconbitmap("D:\\all icons\\file.ico")
root.title('File Cleaner | Devloped By Dhiraj Arya | Dhiraj80')

#=================== Function Deffind ========================

def file_path():
    global path
    path = filedialog.askdirectory()
    sel_ent.insert(0,path)

    item = os.listdir(path)
    i_count=0
    a_count =0
    v_count =0
    d_count =0
    etc_count =0
    for i in item:
        value = i.split('.'[0])
        count = f".{value[1]}".lower()
        if count in imgex_sprt:
            i_count+=1
        elif count in audioex_sprt:
            a_count+=1
        elif count in videoex_sprt:
            v_count+=1
        elif count in docsex_sprt:
            d_count+=1
        else:
            etc_count+=1
        
    img_lbl.config(text=f"Total Image\n{i_count}",compound=TOP,font=("Arial","15",'bold'),fg="#0038ff")
    audio_lbl.config(text=f"Total Audio\n{a_count}",compound=TOP,font=("Arial","15",'bold'),fg="#0038ff")
    video_lbl.config(text=f"Total Video\n{v_count}",compound=TOP,font=("Arial","15",'bold'),fg="#0038ff")
    docs_lbl.config(text=f"Total Document\n{d_count}",compound=TOP,font=("Arial","15",'bold'),fg="#0038ff")
    etc_lbl.config(text=f"Others file\n{etc_count}",compound=TOP,font=("Arial","15",'bold'),fg="#0038ff")

def exit_now():
    q = messagebox.askokcancel("Exit Program",'Quit This Program')
    if "True" in str(q):
        root.destroy()

def slide():
    global f
    try:       
        f-=2
        if f == (-900):
            f = width
        sld_frm.place(x=f,y=106)
        time.sleep(0.02)
        sld_frm.after(1,slide)
    except Exception as a:
        return "None"

def start():
    item = os.listdir(path)
    print(item)
    for m in item:
        value = m.split('.'[0])
        count = f".{value[1]}".lower()
        if count in imgex_sprt:
            pass
        elif count in audioex_sprt:
            pass
        elif count in videoex_sprt:
            pass
        elif count in docsex_sprt:
            pass
        else:
            pass
#================ File icons ==================

t_icon = PhotoImage(file="D:\\all icons\\file.png")
img = PhotoImage(file="D:\\all icons\\img1.png")
audio = PhotoImage(file="D:\\all icons\\mus.png") 
video = PhotoImage(file="D:\\all icons\\video2.png")
docs = PhotoImage(file="D:\\all icons\\docs1.png")
etc = PhotoImage(file="D:\\all icons\\docs.png")

#=========== Heading ==============

title = Label(root,text="File Shorting",image=t_icon,compound=LEFT,fg="white",font=("impact","50"),anchor=W,bg="#1f005a",padx=100)
title.pack(fill=X)

#=========== Select File Path ==============
var = StringVar()

frm1 = Frame(root,pady=60)
frm1.pack(fill=X)

sel_lbl = Label(frm1,text="Select Path",font=("Arial","16"),)
sel_lbl.pack(side=LEFT,padx=70)

sel_ent = Entry(frm1,width=60,borderwidth=1,relief="ridge",bg='#d9d6cd',font=("Arial","16"),textvariable=var)
sel_ent.pack(side=LEFT)

sel_path = Button(frm1,text="Browes File",width=12,relief=FLAT,border=2,bg="black",font=("Arial","16",'bold'),command=file_path,fg="white",cursor="hand2")
sel_path.pack(side=LEFT,padx=30)

#==================== slider ================
f = width
sld_frm= Frame(root,bg="gray",width=1400,height=30)
sld_frm.place(x=f,y=106)
data = "WELCOME TO FILE SHOTING PROJECT   - DEVLOPED BY DHIRAJ ARYA"
sld_text = Label(sld_frm,text=data,bg='yellow',fg="red",font=("Arial","16"))
sld_text.pack()

#================ Seprater Add ===================

Frame(root,bg="gray",width=1250,height=2).pack(fill=X,pady=5,padx=60)

#============== Extanctions frame =================

imgex_sprt = ['Support Image exstinoisan','.png','.jpg','.ico','.bmp']
audioex_sprt = ['Support Audio exstinoisan','.mp3','.wav','.m4a','m4b']
videoex_sprt = ['Support Video exstinoisan','.mp4','.3gp','.mkv','.m2v']
docsex_sprt = ['Support Document exstinoisan','.pdf','.docs','.exle','.pev']

Label(root,text='Various Extention Supports',font=("Arial","25","bold")).pack(fill=X,padx=70,pady=10)

ex_frm = Frame(root,pady=10)
ex_frm.pack(fill=X,padx=90,pady=5)

img_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11","bold"),values=imgex_sprt,state="readonly",justify=CENTER)
img_ex.grid(row=1,column=0,padx=20)
img_ex.current(0)

audio_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11","bold"),values=audioex_sprt,state="readonly",justify=CENTER)
audio_ex.grid(row=1,column=1,padx=20)
audio_ex.current(0)

video_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11","bold"),values=videoex_sprt,state="readonly",justify=CENTER)
video_ex.grid(row=1,column=2,padx=20)
video_ex.current(0)

docs_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11","bold"),values=docsex_sprt,state="readonly",justify=CENTER)
docs_ex.grid(row=1,column=3,padx=20)
docs_ex.current(0)

#================ Seprater Add ===================

Frame(root,bg="gray",width=1250,height=2).pack(fill=X,pady=30,padx=70)

#================ Icons view ================

icon_frm = Frame(root,bg="white",borderwidth=3,relief="ridge")
icon_frm.pack(fill=X,padx=105,pady=5)

img_lbl = Label(icon_frm,image=img,height=220,width=230,bg="#ffc98d")
img_lbl.grid(row=0,column=0)

audio_lbl = Label(icon_frm,image=audio,height=220,width=230,bg="#00ffc9")
audio_lbl.grid(row=0,column=1,padx=4)

video_lbl = Label(icon_frm,image=video,height=220,width=230,bg="#ffee82")
video_lbl.grid(row=0,column=2)

docs_lbl = Label(icon_frm,image=docs,height=220,width=230,bg="#ffe900")
docs_lbl.grid(row=0,column=3,padx=4)

etc_lbl = Label(icon_frm,image=etc,height=220,width=230,bg="#ffae00")
etc_lbl.grid(row=0,column=4)

#================ Button wight ================
            
frm2 = Frame(root,pady=10)
frm2.pack(fill=X,padx=90,pady=30)

start = Button(frm2,text="Start Program",bg="yellow",fg='red',font=("Arial","15","bold"),cursor="hand2",command=start)
start.pack(side=LEFT,pady=20,padx=150)
        
exit = Button(frm2,text="Quit Program",bg="yellow",fg='red',font=("Arial","15","bold"),command=exit_now,cursor="hand2")
exit.pack(side=RIGHT,pady=20,padx=150)
slide()



root.mainloop()