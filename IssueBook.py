import sqlite3
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

# con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
con = sqlite3.connect(mydatabase)
con.execute("CREATE TABLE IF NOT EXISTS issuebook (book_id varchar(20) primary key,issuedto varchar(20))")
cur = con.cursor()

# Enter Table Names here
# issueTable = "books_issued" 
# bookTable = "books"
    
#List To store all Book IDs
allBid = [] 

def issue():
    bid = inf1.get()
    issueto = inf2.get()
    if bid=="" or issueto=="":
        messagebox.showinfo("Unsuccessful","Book id or issued to is missing")
    else:
        cur.execute("SELECT * FROM bookTable WHERE book_id=?",(bid,))
        bid_detail = cur.fetchone()
        if bid_detail !=None:
            if bid_detail[3] == 'avail':
                cur.execute("UPDATE bookTable SET status ='issued' WHERE book_id=?",(bid,))
                con.commit()
                cur.execute("INSERT INTO issuebook (book_id,issuedto) VALUES(?,?)",(bid,issueto))
                con.close()
                messagebox.showinfo("Successful","Book has been issued successfully")
            else:
                messagebox.showinfo("Unsuccessful","Book already issued")
        else:
            print("Didn't get any data")
            



# def issue():
    
#     global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
#     bid = inf1.get()
#     issueto = inf2.get()

#     issueBtn.destroy()
#     labelFrame.destroy()
#     lb1.destroy()
#     inf1.destroy()
#     inf2.destroy()
    
    
#     # extractBid = "select bid from "+bookTable
#     try:
#         cur.execute("SELECT book_id from bookTable")
#         con.commit()
#         for i in cur:
#             allBid.append(i[0])
        
#         if bid in allBid:
#             # checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
#             cur.execute("SELECT status FROM bookTable WHERE book_id=?",(bid,))
#             con.commit()
#             for i in cur:
#                 check = i[0]
                
#             if check == 'avail':
#                 status = True
#             else:
#                 status = False

#         else:
#             messagebox.showinfo("Error","Book ID not present")
#     except:
#         messagebox.showinfo("Error","Can't fetch Book IDs")
    
#     issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
#     show = "select * from "+issueTable
    
#     # updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
#     try:
#         if bid in allBid and status == True:
#             cur.execute(issueSql)
#             con.commit()
#             cur.execute("UPDATE bookTable set status = 'issued' WHERE book_id =?",(bid,))
#             con.commit()
#             messagebox.showinfo('Success',"Book Issued Successfully")
#             root.destroy()
#         else:
#             allBid.clear()
#             messagebox.showinfo('Message',"Book Already Issued")
#             root.destroy()
#             return
#     except:
#         messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
#     print(bid)
#     print(issueto)
    
#     allBid.clear()
    
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
    