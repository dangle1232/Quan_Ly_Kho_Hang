from tkinter import *
import sqlite3
import time
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from tkinter import messagebox
import os

class QL_Kho:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x768+0+0')
        self.root.title("Quan Ly Kho QTC | Dev by Thanh Dang")
        self.root.config(bg="white")

        # Title
        self.icon_title = Image.open("images/qtc.png")
        self.icon_title = self.icon_title.resize((90, 40), Image.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        title = Label(self.root, text="Management Inventory Company QTC", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=30)
        title.place(x=0, y=0, relwidth=1, height=70)

        # btn logout
        btn_logout = Button(self.root, text="Logout",command=self.log_out, font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # clock
        self.lbl_clock = Label(self.root, text="Welcome my app \t\t Date:DD-MM-YYYY\t\t Time :HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # left menu
        self.MenuLogo = Image.open("images/menu_icon.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)
        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        btn_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688")
        btn_menu.pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, text="Employee", font=("times new roman", 20, "bold"), command=self.employee,
                              bg="white", bd=3, cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Product", command=self.product,font=("times new roman", 20, "bold"), bg="white", bd=3,
                             cursor="hand2")
        btn_product.pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier",command=self.supplier, font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category",command=self.category, font=("times new roman", 20, "bold"), bg="white", bd=3,
                              cursor="hand2")
        btn_category.pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales", command=self.sale,font=("times new roman", 20, "bold"), bg="white", bd=3,
                           cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg="white", bd=3,
                          cursor="hand2")
        btn_exit.pack(side=TOP, fill=X)

        # Content
        self.lbl_employee = Label(self.root, text="Employee Details\n [0]", bd=5, relief=RIDGE, bg="#33bbf9",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Category Details\n [0]", bd=5, relief=RIDGE, bg="#ffc107",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=650, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Product Details\n [0]", bd=5, relief=RIDGE, bg="#ff5722",
                                 font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=1000, y=120, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Sales Details\n [0]", bd=5, relief=RIDGE, bg="#009668",
                               font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=300, y=300, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Supplier Details\n [0]", bd=5, relief=RIDGE, bg="#607db8",
                          font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=300, height=150, width=300)


        # footer
        lbl_footer = Label(self.root, text="QTC- Management System || Developed by me",
                           font=("times new roman", 20), bg="#4d636d", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)
        self.update_content()

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)
        
    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
        
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)
        
    def sale(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)
        
    def update_content(self):
        con=sqlite3.connect(database=r'qtc.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Product\n[{str(len(product))}]")
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Supplier\n[{str(len(supplier))}]")
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[{str(len(category))}]")
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[{str(len(employee))}]")
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales [{str(bill)}]')
            
            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config( text=f"Welcome to Kho QTC \t\t Date:{str(date_)}\t\t Time :{str(time_)}")
            self.lbl_clock.after(200,self.update_content)
            
            
        except Exception as ex:
            messagebox.showerror("Error", f"An error occurred: {str(ex)}",parent= self.root)
            
    def log_out(self):
        self.root.destroy()
        os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = QL_Kho(root)
    root.mainloop()
