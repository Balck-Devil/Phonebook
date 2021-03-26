from tkinter import *
import datetime
from View_contact import ViewContact
from addpeople import AddPeople
from aboutus import About

date=datetime.datetime.today().strftime("%d/%m/%Y")
date=str(date)

class Application(object):
    def __init__(self,master):
        self.master=master

        # Frames
        self.top=Frame(master,height=150,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=450,bg="lightgreen")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file=r"D:\PFP\SahilPatel\Python App And Program\Phonebook\phonebook1.png")

        self.top_image_label=Label(self.top,image=self.top_image,bg="White")
        self.top_image_label.place(x=100,y=40)

        self.heading=Label(self.top,text="My Phonebook",font="Times 40 bold",bg="White",fg="Black")
        self.heading.place(x=175,y=40)

        self.date_label=Label(self.top,text=date,font="Times 15 bold",bg="White",fg="black")
        self.date_label.place(x=543,y=5)

        # Buttons        
        self.viewButton=Button(self.bottom,text="  View Contact  ",font="Arial 12 bold",bg="white",fg="green",command=self.view_contact)
        self.viewButton.place(x=260,y=50)

        self.addButton=Button(self.bottom,text="  Add Contact  ",font="Arial 12 bold",bg="white",fg="green",command=self.addpeoplefunction)
        self.addButton.place(x=263,y=120)
        
        self.aboutButton=Button(self.bottom,text="  About Us  ",font="Arial 12 bold",bg="white",fg="green",command=self.about_us)
        self.aboutButton.place(x=275,y=190)

    def view_contact(self):
        contact=ViewContact()

    def addpeoplefunction(self):
        addpeoplewindow=AddPeople()

    def about_us(self):
        aboutpage=About()

def main():
    root=Tk()
    app = Application(root)
    root.title("Phonebook")
    root.geometry("650x550+350+200")
    root.resizable(False,False)

    root.mainloop()

if __name__ == "__main__":
    main()