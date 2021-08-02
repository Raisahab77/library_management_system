import tkinter as tk
from tkinter import Button, Entry, Frame, Label, StringVar, font
from tkinter import messagebox
from tkinter.constants import BOTH, CENTER, FLAT, NE, NW
from typing import Text
import random
import smtplib
import sqlite3
import loginwindow

YourEmail = "Email"
Yourpassword = "Password"
def submit():
    Password = password.get()
    Confirmpassword = confirmPassword.get()
    print(Password)
    if Password == Confirmpassword:
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute("UPDATE registration SET userpassword=? WHERE email =?",(Password,Email))
        conn.commit()
        conn.close()
        messagebox.showinfo("successful","password changed successful")
        root.destroy()
        loginwindow.loginWindow()

def verify():
    # pass
    UserOtp = userotp.get()
    if sentOtp == UserOtp:
        # messagebox.showinfo("successfull")
        global password,confirmPassword
        password = StringVar()
        confirmPassword = StringVar()

        varificationFrame.destroy()
        newFrame = Frame(root,width=400,height=300,bg="white")
        newFrame.place(relx=0.35,rely=0.3)

        passwordLabel = Label(newFrame,text="Password",font=("halvetica",16),bg="white")
        passwordLabel.place(relx=0.1,rely=0.1)
        passwordEntry = Entry(newFrame,font=("halvetica",16),bg="#ede9e8",textvariable=password)
        passwordEntry.place(relx=0.1,rely=0.3,relwidth=0.8)

        confirmPasswordLabel = Label(newFrame,text="Confirm Password",font=("halvetica",16),bg="white")
        confirmPasswordLabel.place(relx=0.1,rely=0.4)
        confirmPasswordEntry = Entry(newFrame,font=("halvetica",16),bg="white",textvariable=confirmPassword)
        confirmPasswordEntry.place(relx=0.1,rely=0.6,relwidth=0.8)

        submitBtn = Button(newFrame,text="Submit",bg="green",command=submit)
        submitBtn.place(relwidth=0.6,relx=0.2,rely=0.8)
    else:
        messagebox.showerror("Error","OTP is wrong")

def sendotp():
    global Email
    Email = email.get()
    if Email != "":
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM registration WHERE email=?",(Email,))
        result = cur.fetchone()
        conn.close()
        if result != None:
            # print(result)    
            global sentOtp, userotp,root,varificationFrame
            s = "0123456789"
            sentOtp = random.sample(s,6)
            sentOtp = "".join(sentOtp)
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login(YourEmail, Yourpassword)

            # message to be sent
            message = sentOtp

            # sending the mail
            s.sendmail(YourEmail, Email, message)

            # terminating the session
            s.quit()
            mainFrame.destroy()
            varificationFrame = Frame(root,width=400,height=300,bg="white")
            varificationFrame.place(relx=0.35,rely=0.3)
            userotp = StringVar()
            otpEntry = Entry(varificationFrame,textvariable=userotp,font=("halvetica",16),bg="#ede9e8",relief=FLAT)
            otpEntry.place(rely=0.1,relx=0.1,relwidth=0.8)
            verifyBtn = Button(varificationFrame,text="Verify",command= verify,font=("times now roman",15,"bold"),bg="navy")
            verifyBtn.place(rely=0.4,relx=0.2,relwidth=0.6)
            root.mainloop()

        else:
            messagebox.showerror("Error","Email is not registerd.")

    else:
        messagebox.showerror("Error","Email feild can't be null")

def forgot_password():
    global root, email, mainFrame
    root = tk.Tk()
    email = StringVar()
    root.config(bg="navy")
    root.title("Forget password")
    root.geometry("1366x720+0+0")
    mainFrame = Frame(root,width=400,height=300,bg="white")
    mainFrame.place(relx=0.35,rely=0.3)
    headLabel = tk.Label(mainFrame,text="Forget Password",font=("times now roman",25,"bold"),fg="black",bg="white")
    headLabel.pack(pady=(40,0),padx=20,anchor=NW)
    emailLabel = tk.Label(mainFrame,text="Email",font=("Arial",15),bg="white")
    emailLabel.pack(pady=(30,0))
    emailEntry = tk.Entry(mainFrame,font=("Arial",15),bg="#ede9e8",borderwidth=0,textvariable=email)
    emailEntry.pack(pady=30,padx=20)
    sendOTPBtn = Button(mainFrame,bg="navy",text="Send OTP",command=sendotp,font=("times now roman",15,"bold"))
    sendOTPBtn.pack(pady=30)
    root.mainloop()

if __name__ =="__main__":
    forgot_password()
