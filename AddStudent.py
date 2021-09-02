import tkinter as tk
from tkinter import Button,ttk,messagebox
import sqlite3
from tkinter.constants import END

def submit():
    if Name.get()=="" or Class.get()=="" or Contact.get()=="" or Email.get()=="":
        messagebox.showerror("Error","All fields are required")

    else:
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS students(student_id PRIMARY KEY,
                                                            name NOT NULL,
                                                            class NOT NULL,
                                                            contact NOT NULL UNIQUE,
                                                            email NOT NULL UNIQUE)""")
        cur.execute("SELECT * FROM students")
        student_id = len(cur.fetchall())
        cur.execute("""INSERT INTO students(student_id,name,class,contact,email)
        VALUES(?,?,?,?,?)""",(student_id,Name.get(),Class.get(),Contact.get(),Email.get()))
        messagebox.showinfo("Successfull",f"You are successfully registerd your student id is {student_id}")
        conn.commit()
        cur.close()
        conn.close()
        nameEntry.delete(0,END)
        classComboBox.delete(0,END)
        contactEntry.delete(0,END)
        emailEntry.delete(0,END)
        

def addStudent():
    global Name, Class, Contact, Email, nameEntry, classComboBox, contactEntry, emailEntry
    root = tk.Tk()
    root.title("Add student")
    root.geometry("1366x720+0+0")
    Name = tk.StringVar()
    Class = tk.StringVar()
    Contact = tk.StringVar()
    Email = tk.StringVar()
    mainFrame = tk.Frame(root,bg="light blue")
    mainFrame.place(rely=0.2,relx=0.3,relheight=0.6,relwidth=0.4)


    nameLabel = tk.Label(mainFrame,text="Name",bg="light blue",font=("Arial",15))
    nameLabel.place(relx=0.2,rely=0.15)
    nameEntry = tk.Entry(mainFrame,width=15,font=("Arial",15),textvariable=Name)
    nameEntry.place(relx=0.5,rely=0.15)


    classLabel = tk.Label(mainFrame,text="Class",bg="light blue",font=("Arial",15))
    classLabel.place(relx=0.2,rely=0.3)
    classComboBox = ttk.Combobox(mainFrame,width=13,font=("Arial",15),textvariable=Class)
    classComboBox['values'] = ('BCA',
                            'BCom',
                            'BBA',
                            'BSc')
    classComboBox.place(relx=0.5,rely=0.3)


    contactLabel = tk.Label(mainFrame,text="Contact",font=("Arial",15),bg="light blue")
    contactLabel.place(relx=0.2,rely=0.45)
    contactEntry = tk.Entry(mainFrame,width=15,font=("Arial",15),textvariable=Contact)
    contactEntry.place(relx=0.5,rely=.45)


    emailLabel = tk.Label(mainFrame,text="Email",font=("Arial",15),bg="light blue")
    emailLabel.place(relx=0.2,rely=0.60)
    emailEntry = tk.Entry(mainFrame,width=15,font=("Arial",15),textvariable=Email)
    emailEntry.place(relx=0.5,rely=.60)

    submitBtn = Button(mainFrame,text="Submit",command = submit)
    submitBtn.place(rely=0.85,relx=0.4,relwidth=0.2)
    root.mainloop()


if __name__ == '__main__':
    addStudent()