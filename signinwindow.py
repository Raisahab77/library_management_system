import tkinter as tk
from tkinter.constants import CENTER, RIDGE
from tkinter import messagebox
import sqlite3

def login():
    root.destroy()
    from loginwindow import loginWindow
    loginWindow()

def signUp():
    Name = name.get()
    Username = username.get()
    Email = email.get()
    Password = password.get()
    Confirmpassword = confirmpassword.get()
    
    
    # cur.execute("""CREATE TABLE IF NOT EXISTS registration (name varchar(20) , username varchar(30) primary key, password varchar(30))""")
    # cur.execute("insert into registration (name,username,password) values(?,?,?)",(Name,Username,Password))
    if Name =="" or Username =="" or Email == "" or Password =="" or Confirmpassword =="":
        messagebox.showerror("Error","All fileds are required !")
    else:
        if Confirmpassword!=Password:
            messagebox.showerror("Error","Password and Confirm password doesn't match")
        else:
            # try:
            print("reached in trying")
            conn = sqlite3.connect("main.db")
            cur = conn.cursor()
            # conn.close()
            cur.execute("""CREATE TABLE IF NOT EXISTS registration (fullname varchar(20), username varchar(30), email varchar(30) primary key, userpassword varchar(30))""")
            print("Table created")
            cur.execute("INSERT INTO registration (fullname, username, email, userpassword) VALUES (?,?,?,?)",(Name,Username,Email,Password))
            print("Insertion successful")
            conn.commit()
            conn.close()
            print(f"name is {Name},username is {Username},Email is {Email},password is {Password},confirm password is {Confirmpassword}")
            messagebox.showinfo("Success","Congrats your registration is successful.")
            # except:
            #     messagebox.showerror("Error","Registration is unsuccessful change user name")

def signUpwindow():
    global root, name,username,email,password,confirmpassword, signUpframe
    root = tk.Tk()
    root.geometry("1370x720+0+0")
    root.config(bg="white")
    name = tk.StringVar()
    username = tk.StringVar()
    email = tk.StringVar()
    password = tk.StringVar()
    confirmpassword = tk.StringVar()
    # left_bg_frame = tk.Frame(root,bg="#40e3e3")
    # left_bg_frame.place(relwidth=0.4,relheight=1)
    # right_bg_frame = tk.Frame(root,bg="black")
    # right_bg_frame.place(relx=0.4,rely=0,relwidth=1,relheight=1)
    
    leftFrame = tk.Frame(root,bg="navy")
    leftFrame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.5)
    signUpframe = tk.Frame(root,bg="white",relief=RIDGE,bd=1)
    signUpframe.place(relx=0.6,rely=0.1,relheight=0.8,relwidth=0.37)
    signUpLbl = tk.Label(signUpframe,text="Sign Up",font=("times roman now",25,"bold"),bg="white")
    signUpLbl.place(relx=0.4,rely=0.06)

    #---------------------------------- Label -----------------------------------------
    nameLabel = tk.Label(signUpframe,text="Name",font=("times roman now",13),bg="white")
    nameLabel.place(relx=0.1,rely=0.18)
    nameEntry = tk.Entry(signUpframe,text="Name",font=("times roman now",13),bg="white",textvariable=name)
    nameEntry.place(relx=0.5,rely=0.18)


    userNameLabel = tk.Label(signUpframe,text="User Name",font=("times roman now",13),bg="white")
    userNameLabel.place(relx=0.1,rely=0.27)
    userNameEntry = tk.Entry(signUpframe,text="User Name",font=("times roman now",13),bg="white",textvariable=username)
    userNameEntry.place(relx=0.5,rely=0.27)
    
    emailNameLabel = tk.Label(signUpframe,text="Email",font=("times roman now",13),bg="white")
    emailNameLabel.place(relx=0.1,rely=0.36)
    emailNameEntry = tk.Entry(signUpframe,text="Email",font=("times roman now",13),bg="white",textvariable=email)
    emailNameEntry.place(relx=0.5,rely=0.36)
    
    
    passwordLabel = tk.Label(signUpframe,text="Password",font=("times roman now",13),bg="white")
    passwordLabel.place(relx=0.1,rely=0.45)
    passwordEntry = tk.Entry(signUpframe,text="Password",font=("times roman now",13),bg="white",textvariable=password)
    passwordEntry.place(relx=0.5,rely=0.45)
    
    
    confirmPasswordLabel = tk.Label(signUpframe,text="Confirm Password",font=("times roman now",13),bg="white")
    confirmPasswordLabel.place(relx=0.1,rely=0.54)
    confirmPasswordEntry = tk.Entry(signUpframe,text="Confirm Password",font=("times roman now",13),bg="white",textvariable=confirmpassword)
    confirmPasswordEntry.place(relx=0.5,rely=0.54)

    signUpBtn = tk.Button(signUpframe,text="Sign Up",bg="navy",fg="white",font=("Helvetica",12),width=20,command=signUp)
    signUpBtn.place(relx=0.3,rely=0.66)

    hr = tk.Label(signUpframe,bg="lightgray")
    hr.place(rely=0.8,relwidth=1,height=2)
    or_ = tk.Label(signUpframe,fg="gray",text="OR",bg="white",font=("cursiv",8,"bold"))
    or_.place(relx=0.5,rely=0.782)

    loginLbl = tk.Label(signUpframe,text="Already have an account?",bg="white")
    loginLbl.place(relx=0.3,rely=0.9)
    loginBtn = tk.Button(signUpframe,text="Login",fg="blue",bg="white",bd=0,command=login)
    loginBtn.place(relx=0.58,rely=0.9)

    root.mainloop()

if __name__ == '__main__':    
    signUpwindow()