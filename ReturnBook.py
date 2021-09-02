from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3





allBid = [] #List To store all Book IDs

def returnBtn():
    bid = bookInfo1.get()
    if bid=="":
        messagebox.showinfo("Unsuccessful","Book id is missing")
    else:
        con = sqlite3.connect("main.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM bookTable WHERE book_id=?",(bid,))
        bid_detail = cur.fetchone()
        if bid_detail != None:
            if bid_detail[3] == 'issued':
                cur.execute("UPDATE bookTable SET status ='avail' WHERE book_id=?",(bid,))
                con.commit()
                cur.execute("DELETE FROM issuebook WHERE book_id=?",(bid,))
                con.commit()
                con.close()
                messagebox.showinfo("Successful","You have successfully returned book")
            else:
                messagebox.showinfo("Unsuccessful","Book already returned")
        else:
            print("Didn't not get any data")
# def returnn():
    
#     global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
#     

#     extractBid = "select bid from "+issueTable
#     try:
#         cur.execute(extractBid)
#         con.commit()
#         for i in cur:
#             allBid.append(i[0])
        
#         if bid in allBid:
#             checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
#             cur.execute(checkAvail)
#             con.commit()
#             for i in cur:
#                 check = i[0]
                
#             if check == 'issued':
#                 status = True
#             else:
#                 status = False

#         else:
#             messagebox.showinfo("Error","Book ID not present")
#     except:
#         messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
#     issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"
  
#     print(bid in allBid)
#     print(status)
#     updateStatus = "update "+bookTable+" set status = 'avail' where bid = '"+bid+"'"
#     try:
#         if bid in allBid and status == True:
#             cur.execute(issueSql)
#             con.commit()
#             cur.execute(updateStatus)
#             con.commit()
#             messagebox.showinfo('Success',"Book Returned Successfully")
#         else:
#             allBid.clear()
#             messagebox.showinfo('Message',"Please check the book ID")
#             root.destroy()
#             return
#     except:
#         messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
#     allBid.clear()
#     root.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#bf1c19")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#bf1c19",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='#bf1c19', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='#bf1c19')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='#bf1c19', fg='white',font=("Arial",15))
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame,font=("Arial",15))
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnBtn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

if __name__ == '__main__':
    returnBook()
    