import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


# con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
con = sqlite3.connect("main.db")
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
# bookTable = "books" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()
    
    # deleteSql = "delete from "+bookTable+" where book_id = '"+bid+"'"
    # deleteIssue = "delete from "+issueTable+" where book_id = '"+bid+"'"
    try:
        cur.execute("DELETE FROM bookTable WHERE book_id=?",(bid,))
        con.commit()
        # cur.execute(deleteIssue)
        con.close()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#050245")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#050245",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='#050245', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg="#050245")
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='#050245', fg='white',font=("Arial",15))
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame,font=("Arial",15))
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.5)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

if __name__ == '__main__':
    delete()
    