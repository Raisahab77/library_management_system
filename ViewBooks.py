from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


mypass = "root"
mydatabase="db"

con = sqlite3.connect(mydatabase)
cur = con.cursor()


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("",END,values=i)

def View(): 
    global trv
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1366x720")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#12a4d9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='#12a4d9', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    trv = ttk.Treeview(labelFrame,columns=(1,2,3,4),show="headings",height="0.4")
    trv.pack(fill=BOTH,expand=1)
    trv.heading(1,text="Book ID")
    trv.heading(2,text="Title")
    trv.heading(3,text="Author")
    trv.heading(4,text="Status")

    try:
        cur.execute("SELECT * FROM bookTable")
        rows = cur.fetchall()
        con.commit()
        update(rows)
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

if __name__ == '__main__':
    View()
    