from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
import sqlite3

con = sqlite3.connect(mydatabase)
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS bookTable (book_id varchar(20) primary key, book_title varchar(30), author varchar(30), status varchar(30))""")

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("1366x720")

frame = Frame(root,bg="white")
frame.place(relheight=1,relwidth=1)

bg = ImageTk.PhotoImage(file="library.jpg")

photo = PhotoImage(file="buttons.png")
resizeImg = photo.subsample(5,5)
# Create a Canvas
canvas = Canvas(frame, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# Add Image inside the Canvas
canvas.create_image(0, 0, image=bg, anchor='nw')

btn1 = Button(frame,text="Add Book Details",bg='black',image=resizeImg, fg='white', command=addBook,relief=FLAT,compound=CENTER)
btn1.place(relx=0.45,rely=0.2)
    
btn2 = Button(frame,text="Delete Book",bg='black', fg='white',image=resizeImg, command=delete,relief=FLAT,compound=CENTER)
btn2.place(relx=0.45,rely=0.35)
    
btn3 = Button(frame,text="View Book List",bg='black', fg='white',image=resizeImg, command=View,relief=FLAT,compound=CENTER)
btn3.place(relx=0.45,rely=0.5)
    
btn4 = Button(frame,text="Issue Book to Student",bg='black', fg='white',image=resizeImg, command = issueBook,relief=FLAT,compound=CENTER)
btn4.place(relx=0.45,rely=0.65)
    
btn5 = Button(frame,text="Return Book",bg='black', fg='white',image=resizeImg, command = returnBook,relief=FLAT,compound=CENTER)
btn5.place(relx=0.45,rely=0.80)

root.mainloop()