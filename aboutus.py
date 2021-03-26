from tkinter import *

class About(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("550x550+450+100")
        self.title("About Us")
        self.resizable(False,False)

        self.top=Frame(self,height=550,width=550 ,bg="red")
        self.top.pack(fill=BOTH)
        
        self.text=Label(self.top,text="Hey This Is About Us Page !!! \n \n \n \n This Phonebook Is Use For Save Numbers And Other Details SO You Can Use It \n This Application Is  Made For Education Purpose \n You Can Contact Us On Facebook Or Instagram",font="Arial 10 bold",bg="red",fg="white")
        self.text.place(x=18,y=150)