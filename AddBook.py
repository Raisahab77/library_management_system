import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status =selected.get()
   
    if bid =="" or title =="" or author =="" or status =="":
        messagebox.showerror("Error","All fileds are required !")
    else:
        try:
            con = sqlite3.connect("main.db")
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS bookTable (book_id varchar(20) PRIMARY KEY,
                                                                book_title varchar(50),
                                                                author varchar(30),
                                                                status varchar(10))""")
            cur.execute("insert into bookTable (book_id,book_title,author,status) values(?,?,?,?)",(bid,title,author,status))
            con.commit()
            messagebox.showinfo('Success',"Book added successfully")
            cur.close()
            con.close()
            print(bid)
            print(title)
            print(author)
            print(status)
        except Exception as e:
            print(e)
            messagebox.showerror("Error","Can't add data into Database")
    

    
def addBook(): 
    
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root, selected
    root = Tk()
    selected = StringVar()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    headingFrame1 = Frame(root,bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", fg='green', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg="navy")
    labelFrame.place(relx=0.1,rely=0.2,relwidth=0.8,relheight=0.6)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='navy', fg='white',font=("Arial",15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame,font=("Arial",15))
    bookInfo1.place(relx=0.5,rely=0.2, relwidth=0.45,relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='navy', fg='white',font=("Arial",15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame,font=("Arial",15))
    bookInfo2.place(relx=0.5,rely=0.35, relwidth=0.45, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='navy', fg='white',font=("Arial",15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame,font=("Arial",15))
    bookInfo3.place(relx=0.5,rely=0.50, relwidth=0.45, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status : ", bg='navy', fg='white',font=("Arial",15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    
    s = ttk.Style()
    s.configure('Wild.TRadiobutton',    # First argument is the name of style. Needs to end with: .TRadiobutton
        background="navy",         # Setting background to our specified color above
        foreground = "white")
    r1 = ttk.Radiobutton( text='Avaliable', value="avaliable", variable=selected,style = 'Wild.TRadiobutton')
    r1.place(relx =.5, rely=0.6 ,relwidth=.17)

    r2 = ttk.Radiobutton( text='Issued', value="issued", variable=selected,style = 'Wild.TRadiobutton')
    r2.place(relx =.71, rely=0.6 ,relwidth=.17)

    # r1 = ttk.Radiobutton( text='Male', value="male", variable=selected)
    # r1.place(relx =.5, rely=0.6 ,relwidth=.17)
    # r2 = ttk.Radiobutton( text='Female', value="female", variable=selected)
    # r2.place(relx =.71, rely=0.6 ,relwidth=.17)
    # bookInfo4 = Entry(labelFrame,font=("Arial",15))
    # bookInfo4.place(relx=0.5,rely=0.65, relwidth=0.45, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


if __name__ == '__main__':
    addBook()
    