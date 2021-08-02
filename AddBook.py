import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    # insertBooks = f"insert into + {bookTable} +(book_id,book_title,author,status) values(?,?,?,?)",(bid,title,author,status)
    try:
        cur.execute("insert into bookTable (book_id,book_title,author,status) values(?,?,?,?)",(bid,title,author,status))
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(bid)
    print(title)
    print(author)
    print(status)


    root.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="db"

    # con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    con = sqlite3.connect(mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    bookTable = "books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='green', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=("Arial",15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame,font=("Arial",15))
    bookInfo1.place(relx=0.5,rely=0.2, relwidth=0.45,relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white',font=("Arial",15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame,font=("Arial",15))
    bookInfo2.place(relx=0.5,rely=0.35, relwidth=0.45, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white',font=("Arial",15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame,font=("Arial",15))
    bookInfo3.place(relx=0.5,rely=0.50, relwidth=0.45, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white',font=("Arial",15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame,font=("Arial",15))
    bookInfo4.place(relx=0.5,rely=0.65, relwidth=0.45, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


if __name__ == '__main__':
    addBook()
    