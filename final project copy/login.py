from logging import root
from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox 

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1350x690+0+3")

#======================bgimage========================
#======================frame=====================
        frame=Frame(self.root,bg="white",bd=10,relief=RIDGE)
        frame.place(x=500,y=100,width=350,height=400)

        get_str=Label(frame,text="get started",font=("times new roman",10,"bold"),fg="white",bg="black")
        get_str.place(x=50,y=90)


        username=lbl=Label(frame,text="username",font=("times new roman",10,"bold"),fg="white",bg="black")
        username.place(x=30,y=120)

        self.textuser=Entry(frame,font=("times new roman",10,"bold"))
        self.textuser.place(x=90,y=120)

        password=lbl=Label(frame,text="password",font=("times new roman",10,"bold"),fg="white",bg="black")
        password.place(x=30,y=150)

        self.textpassword=Entry(frame,font=("times new roman",10,"bold"))
        self.textpassword.place(x=100,y=160)

        loginbtn=Button(frame,text="login",font=("times new roman",10,"bold"),command=self.ilogin,bd=5,fg="red",bg="white")
        loginbtn.place(x=95,y=200)

        forgotbtn=Button(frame,text="forgot password",font=("times new roman",10,"bold"),bd=5,fg="red",bg="white")
        forgotbtn.place(x=95,y=230)

    def ilogin(self):

        uname=self.textuser.get
        pwd= self.textpassword.get

        if self.textuser.get=="" or self.textpassword.get()=="":
            messagebox.showerror("Error","all field's are required")

        elif self.textuser.get()=="pratik" and self.textpassword.get()=="pratik123":
            messagebox.showinfo("Success","welcome")
        else: 
             messagebox.showerror("Invalid","invalid user or pass")


if __name__ == "__main__":
 root=Tk()
 app=login(root)
 root.mainloop()

