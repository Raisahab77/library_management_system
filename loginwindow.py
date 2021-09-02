import tkinter as tk
from tkinter import *
from tkinter import Button, Frame, Label, messagebox, StringVar, font
from tkinter.constants import RIDGE
from PIL import ImageTk, Image
import sqlite3
import forgetPassword

def login():
    emailvalue = email.get()
    passwordvalue =password.get()
    if emailvalue=="" or passwordvalue=="":
        messagebox.showerror("Error","All fileds are required !")
    else:
        try:
            conn = sqlite3.connect("main.db")
            cur = conn.cursor()
            cur.execute("SELECT email,userpassword FROM registration where email=?",(emailvalue,))
            result = cur.fetchone()
            conn.close()
            if emailvalue==result[0] and passwordvalue == result[1]:
                # messagebox.showinfo("Successful","You have logged in successfully")
                root.destroy()
                import main
            else:
                messagebox.showerror("Error","User name or password doesn't match!")
        except Exception as e:
            print(e)
        # cur.execute("SELECT username and password fr")

def forgetPass():
    root.destroy()
    forgetPassword.forgot_password()

def signUpWindow():
    root.destroy()
    from signinwindow import signUpwindow
    signUpwindow()

def loginWindow():
    global root,email, password
    root = tk.Tk()
    email =  StringVar()
    password = StringVar()
    root.config(bg="light pink")
    root.title("Login Window")
    root.geometry("1366x720")
    # root.resizable(False,False)
    #--------------- Registration frame-----------------------------------------------

    # Open the Image File
    # bg = ImageTk.PhotoImage(file="library.jpg")

    # # Create a Canvas
    # canvas = Canvas(root, width=700, height=3500)
    # canvas.pack(fill=BOTH, expand=True)

    # # Add Image inside the Canvas
    # canvas.create_image(0, 0, image=bg, anchor='nw')


    # def resize_image(e):
    #     global image, resized, image2
    #     # open image to resize it
    #     image = Image.open("library.jpg")
    #     # resize the image with width and height of root
    #     resized = image.resize((e.width, e.height), Image.ANTIALIAS)

    #     image2 = ImageTk.PhotoImage(resized)
    #     canvas.create_image(0, 0, image=image2, anchor='nw')


    # root.bind("<Configure>", resize_image)

    # welcomeLabel = Label(root,text="Welcome to\nthe Library",font=("times now roman",25,"bold"))
    # welcomeLabel.place(relx=0.3,rely=0.4)

    regFrame = tk.Frame(root,bg="white",borderwidth=1,relief=RIDGE)
    regFrame.place(relx=0.34,rely=0.15,relheight=0.6,relwidth=0.3)


    titleLabel = tk.Label(regFrame,text="Login",font=("Arial",20,"bold"),bg="white")
    titleLabel.place(rely=0.05,relx=0.4)
    EmailNameLabel = tk.Label(regFrame,text="Email",font=("Arial",15),bg="white")
    EmailNameLabel.place(rely=0.15,relx=0.25)
    EmailNameEntry = tk.Entry(regFrame,font=("Arial",15),bg="#ede9e8",borderwidth=0,textvariable=email)
    EmailNameEntry.place(rely=0.25,relx=0.25)
    passwordLabel = tk.Label(regFrame,text="Password",font=("Arial",15),bg="white")
    passwordLabel.place(rely=0.35,relx=0.25)
    passwordEntry = tk.Entry(regFrame,font=("Arial",15),bg="#ede9e8",borderwidth=0,textvariable=password)
    passwordEntry.place(rely=0.45,relx=0.25)

    loginBtn = Button(regFrame,text="Login",bg="#63f7ff",font=("Helvetica",12),command=login)
    loginBtn.place(rely=0.64,relx=0.3,relwidth=0.4)

    hr = Label(regFrame,bg="lightgray")
    hr.place(rely=0.8,relwidth=1,height=2)
    or_ = Label(regFrame,fg="gray",text="OR",bg="white",font=("cursiv",8,"bold"))
    or_.place(rely=0.787,relx=0.5)

    forgetPasswordBtn = Button(regFrame,text="Forget password ?",fg="blue",bg="white",bd=0,command=forgetPass)
    forgetPasswordBtn.place(rely=0.51,relx=0.5)

    signUpLbl = Label(regFrame,text="Don't have an account?",bg="white")
    signUpLbl.place(rely=0.88,relx=0.28)
    
    signUpBtn = Button(regFrame,text="Sign up",fg="blue",bg="white",bd=0,command=signUpWindow)
    signUpBtn.place(rely=0.88,relx=0.6)

    root.mainloop()


if __name__ == '__main__':
    loginWindow()