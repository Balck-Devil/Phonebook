from tkinter import *
import sqlite3
from addpeople import AddPeople
from updatepeople import Update
from tkinter import messagebox
from display import Display

con=sqlite3.connect("database.db")
cur=con.cursor()

class ViewContact(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        self.geometry("650x650+600+100")
        self.title("View Contact")
        self.resizable(False,False)

        self.top=Frame(self,height=150,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(self,height=450,bg="orange")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file=r"D:\PFP\SahilPatel\Python App And Program\Phonebook\team.png")

        self.top_image_label=Label(self.top,image=self.top_image,bg="White")
        self.top_image_label.place(x=100,y=40)

        self.heading=Label(self.top,text="View Contact",font="Times 40 bold",bg="White",fg="Black")
        self.heading.place(x=175,y=40)

        self.scroll=Scrollbar(self.bottom,orient=VERTICAL)

        self.listBox=Listbox(self.bottom,width=50,height=30)
        self.listBox.grid(row=0,column=0,padx=(40,0))
        self.scroll.config(command=self.listBox.yview)
        self.listBox.config(yscrollcommand=self.scroll.set)

        persons=cur.execute("select * from 'Address'").fetchall()
        count=0
        for person in persons:
            self.listBox.insert(count,str(person[0])+" "+person[1]+" "+person[2])
            count+=1

        self.scroll.grid(row=0,column=1,sticky=N+S)

        btnadd=Button(self.bottom,text="Add",width=12,font="Arial 12 bold",command=self.add_people,fg="orange")
        btnadd.grid(row=0,column=2,padx=75,pady=10,sticky=N)

        btnupdate=Button(self.bottom,text="Update",width=12,font="Arial 12 bold",fg="orange",command=self.update_function)
        btnupdate.grid(row=0,column=2,padx=75,pady=70,sticky=N)

        btndisplay=Button(self.bottom,text="Display",width=12,font="Arial 12 bold",fg="orange",command=self.display_people)
        btndisplay.grid(row=0,column=2,padx=75,pady=130,sticky=N)

        btndelete=Button(self.bottom,text="Delete",width=12,font="Arial 12 bold",fg="orange",command=self.delete_person)
        btndelete.grid(row=0,column=2,padx=75,pady=190,sticky=N)

    def add_people(self):
        add_page =AddPeople()
        self.destroy()

    def update_function(self):
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id=person.split(" ")[0]
        updatepage=Update(person_id)

    def display_people(self):
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id=person.split(" ")[0]
        displaypage=Display(person_id)

    def delete_person(self):
        selected_item=self.listBox.curselection()
        person=self.listBox.get(selected_item)
        person_id=person.split(" ")[0]

        query="delete from Address where person_id = {}".format(person_id)
        answer=messagebox.askquestion("Warning","Are You Sure You Want To Delete ?")
        if answer=="yes":
            try:
                cur.execute(query)
                con.commit()
                messagebox.showinfo("Success","Deleted")
                self.destroy()
            except Exception as E:
                messagebox.showinfo("Info",str(E))