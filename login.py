from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry('1350x768+0+0')
        self.root.config(bg="#fafafa")
        
        # Image
        self.phone_image = ImageTk.PhotoImage(file='images/cate.png')
        self.lbl_Phone_image = Label(self.root, image=self.phone_image, bd=0)
        self.lbl_Phone_image.place(x=200, y=50)
        
        # Login Frame
        self.employee_id = StringVar()
        self.password = StringVar()
        
        login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="#e6e6e6")
        login_frame.place(x=510, y=90, width=350, height=460)
        
        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), bg="white", fg="#333333")
        title.place(x=40, y=100)
        
        lbl_user = Label(login_frame, text="Employee ID:", font=("Andalus", 15), bg="#e6e6e6", fg="#333333")
        lbl_user.place(x=20, y=200)

        txt_employee_id = Entry(login_frame, textvariable=self.employee_id, font=("Times New Roman", 12))
        txt_employee_id.place(x=150, y=200)
        
        lbl_pass = Label(login_frame, text="Password:", font=("Andalus", 15), bg="#e6e6e6", fg="#333333")
        lbl_pass.place(x=20, y=250)
        
        txt_password = Entry(login_frame, textvariable=self.password, font=("Times New Roman", 12), show="*")
        txt_password.place(x=150, y=250)
        
        btn_login = Button(login_frame, text="Log In", font=("Arial", 12), bg="#4caf50", fg="white", command=self.login)
        btn_login.place(x=150, y=300)
        
        btn_forgot = Button(login_frame, text="Forgot Password", font=("Arial", 12), bg="#f44336", fg="white", command=self.forgot_password)
        btn_forgot.place(x=110, y=350)
    
    def login(self):
        con = sqlite3.connect(database=r'qtc.db')
        cur = con.cursor()
        try:
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                cur.execute("SELECT utype FROM employee WHERE eid=? AND pass=?", (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()
                if user == None:
                    messagebox.showerror("Error", "Invalid Username/Password", parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def forgot_password(self):
        # Implement the logic for the "Forgot Password" functionality here
        # Open a new window or dialog for password recovery/reset
        messagebox.showinfo("Forgot Password", "Please contact the administrator to reset your password.")

root = Tk()
obj = Login_System(root)
root.mainloop()
