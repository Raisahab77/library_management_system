import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

allBid = [] 

def issue():
    bid = inf1.get()
    issueto = int(inf2.get())
    
    print(type(issueto))
    if bid=="" or issueto=="":
        messagebox.showinfo("Unsuccessful","Book id or issued to is missing")
    else:
        con = sqlite3.connect("main.db")
        con.execute("CREATE TABLE IF NOT EXISTS issuebook (book_id varchar(20) primary key,issuedto integer(20))")
        cur = con.cursor()
        cur.execute("SELECT * FROM bookTable WHERE book_id=?",(bid,))
        bid_detail = cur.fetchone()
        if bid_detail !=None:
            if bid_detail[3] == 'avail':
                cur.execute("SELECT * FROM students WHERE student_id=?",(issueto,))
                result = cur.fetchone()
                if result!=None:
                    cur.execute("UPDATE bookTable SET status ='issued' WHERE book_id=?",(bid,))
                    con.commit()
                    cur.execute("INSERT INTO issuebook (book_id,issuedto) VALUES(?,?)",(bid,issueto))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Successful","Book has been issued successfully")
                else:
                    messagebox.showinfo("Unregisterd","Not Registerd User")
                    print("Student is not registerd")
                
            else:
                messagebox.showinfo("Unsuccessful","Book already issued")
        else:
            print("Didn't get any data")

def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='#c48c12', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='#c48c12',font=("Arial",15))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame,font=("Arial",15))
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='#c48c12',font=("Arial",15))
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame,font=("Arial",15))
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

if __name__ == '__main__':
    issueBook()
    