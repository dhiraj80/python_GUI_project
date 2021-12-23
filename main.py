from tkinter import *
from tkinter import ttk,messagebox,filedialog
from PIL import Image,ImageTk

class Gui(Tk):
    def __init__(self):
        super().__init__()

        height = self.winfo_screenheight()
        width = self.winfo_screenwidth()
        self.geometry(f"{width}x{height}+0+0")
        self.wm_iconbitmap("D:\\all icons\\file.ico")
        self.title('File Cleaner | Devloped By Dhiraj Arya | Dhiraj80')

        t_icon = PhotoImage(file="D:\\all icons\\file.png")
        #=========== Heading ==============
        title = Label(self,text="File Shorting",fg="white",font=("impact","50"),anchor=W,bg="#1f005a",padx=100)
        title.pack(fill=X)

        #=========== Select File Path ==============
        global sel_ent
        var = StringVar()

        frm1 = Frame(self,pady=50)
        frm1.pack(fill=X)

        sel_lbl = Label(frm1,text="Select Path",font=("Arial","16"),)
        sel_lbl.pack(side=LEFT,padx=80)

        sel_ent = Entry(frm1,width=120,borderwidth=5,relief=FLAT,bg='#d9d6cd',highlightbackground="black",font=("Arial","10",'bold'),textvariable=var)
        sel_ent.pack(side=LEFT)

        sel_path = Button(frm1,text="Browes File",width=15,relief=FLAT,border=2,bg="black",font=("Arial","12",'bold'),command=file_path,fg="white")
        sel_path.pack(side=LEFT,padx=80)

        #================ Seprater Add ===================
        Frame(self,bg="gray",width=1250,height=2).pack(fill=X,pady=5,padx=70)

        #============== Extanctions frame =================
        Label(self,text='Various Extention Supports',font=("Arial","25","bold")).pack(fill=X,padx=70,pady=10)

        ex_frm = Frame(self,pady=10)
        ex_frm.pack(fill=X,padx=90,pady=5)

        img_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11"))
        img_ex.grid(row=1,column=0,padx=20)

        audio_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11"))
        audio_ex.grid(row=1,column=1,padx=20)

        video_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11"))
        video_ex.grid(row=1,column=2,padx=20)

        docs_ex = ttk.Combobox(ex_frm,width=30,font=("Arial","11"))
        docs_ex.grid(row=1,column=3,padx=20)

        #================ Seprater Add ===================
        Frame(self,bg="gray",width=1250,height=2).pack(fill=X,pady=30,padx=70)

        #================ Icons view ================
        img = PhotoImage(file="D:\\all icons\\img1.png")
        audio = PhotoImage(file="D:\\all icons\\mus.png") 
        video = PhotoImage(file="D:\\all icons\\video2.png")
        docs = PhotoImage(file="D:\\all icons\\docs1.png")
        etc = PhotoImage(file="D:\\all icons\\docs.png")

        icon_frm = Frame(self,bg="red")
        icon_frm.pack(fill=X,padx=90,pady=5)

        img_lbl = Label(icon_frm,image=img)
        img_lbl.grid(row=0,column=0)

        audio_lbl = Label(icon_frm,image=audio)
        audio_lbl.grid(row=0,column=1)

        video_lbl = Label(icon_frm,image=video)
        video_lbl.grid(row=0,column=2)

        docs_lbl = Label(icon_frm,image=docs)
        docs_lbl.grid(row=0,column=3)

        etc_lbl = Label(icon_frm,image=etc)
        etc_lbl.grid(row=0,column=4)

        #================ Button wight ================
        def exit_now():
            q = messagebox.askokcancel("Exit Program",'Quit This Program')
            if "True" in str(q):
                self.destroy()            

        frm2 = Frame(self,pady=10)
        frm2.pack(fill=X,padx=90,pady=5)

        start = Button(frm2,text="Start Program",bg="yellow",fg='red',font=("Arial","15","bold"),cursor="hand2")
        start.pack(side=LEFT,pady=20,padx=150)
        
        exit = Button(frm2,text="Quit Program",bg="yellow",fg='red',font=("Arial","15","bold"),command=exit_now,cursor="hand2")
        exit.pack(side=RIGHT,pady=20,padx=150)

        
    #=================== Function Deffind ========================
    #=================== Function Started ========================
    global file_path

    def file_path():
        path = filedialog.askdirectory()
        print(path)
        if path == "":

            t = messagebox.OKCANCEL("Folder Not Selectd",'Do not Selected file/Folder Please Selected Now')
        else:
            sel_ent.insert(0,path)  


obj = Gui()
obj.mainloop()