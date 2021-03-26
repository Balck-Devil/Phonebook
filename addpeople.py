from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect("database.db")
cur=con.cursor()

class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+500+100")
        self.title("Add New Person")
        self.resizable(False,False)

        self.top=Frame(self,height=150,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=480,bg="purple")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file=r"D:\PFP\SahilPatel\Python App And Program\Phonebook\add.png")

        self.top_image_label=Label(self.top,image=self.top_image,bg="White")
        self.top_image_label.place(x=100,y=40)

        self.heading=Label(self.top,text="Add New People",font="Times 40 bold",bg="White",fg="Black")
        self.heading.place(x=175,y=40)

        #  Name
        self.label_name=Label(self.bottom,text="Name",font="Arial 15 bold",bg="white",fg="purple")
        self.label_name.place(x=50,y=50)

        self.entry_name=Entry(self.bottom,width=40,bd=2)
        self.entry_name.insert(0,"Enter Name")
        self.entry_name.place(x=150,y=50)

        # surname
        self.label_surname=Label(self.bottom,text="Surname",font="Arial 15 bold",bg="white",fg="purple")
        self.label_surname.place(x=50,y=100)

        self.entry_surname=Entry(self.bottom,width=40,bd=2)
        self.entry_surname.insert(0,"Enter Surname")
        self.entry_surname.place(x=150,y=100)

        #  Num
        self.label_num=Label(self.bottom,text="Number",font="Arial 15 bold",bg="white",fg="purple")
        self.label_num.place(x=50,y=150)

        self.entry_num=Entry(self.bottom,width=40,bd=4)
        self.entry_num.insert(0,"Enter Number")
        self.entry_num.place(x=150,y=150)

        # Email
        self.label_email=Label(self.bottom,text="Email",font="Arial 15 bold",bg="white",fg="purple")
        self.label_email.place(x=50,y=200)

        self.entry_email=Entry(self.bottom,width=40,bd=4)
        self.entry_email.insert(0,"Enter Email")
        self.entry_email.place(x=150,y=200)

        # Address
        self.label_address=Label(self.bottom,text="Address",font="Arial 15 bold",bg="white",fg="purple")
        self.label_address.place(x=50,y=250)

        self.entry_address=Text(self.bottom,width=40,height=7,bd=4)
        self.entry_address.place(x=150,y=250)

        button=Button(self.bottom,text="Add Person",bg="white",font="Arial 15 bold",command=self.add_people,fg="purple")
        button.place(x=250,y=425)

    def add_people(self):
        name =self.entry_name.get()
        surname=self.entry_surname.get()
        email=self.entry_email.get()
        phone=self.entry_num.get()
        address=self.entry_address.get(1.0,"end-1c")

        if name and surname and email and phone and address !="":
            try:
                # Address(Person_ID,Person_Name,Person_Surname,Person_Email,Person_Phone,Person_Address) vaues()
                query="insert into 'Address'(Person_Name,Person_Surname,Person_Email,Person_Phone,Person_Address) values(?,?,?,?,?) "
                cur.execute(query,(name,surname,email,phone,address))
                con.commit()
                messagebox.showinfo("Success","Contact Added")
            except Exception as E:
                messagebox.showerror("Error",str(E))

        else:
            messagebox.showerror("Error","Fill The All Fields",icon="warning")