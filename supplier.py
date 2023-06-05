from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
class supplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1100x500+220+130')
        self.root.title("Quan Ly Kho QTC | Dev by Thanh Dang")
        self.root.config (bg="white")
        self.root.focus_force()
        #All Var
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        

        
        #===searchFrame
       
        
        
        ## ===Options
        lbl_search =Label(self.root,text="Invoice No", bg="white",font=("goudy old style",15))
        lbl_search.place (x=700,y=80)
        txt_search=Entry(self.root,textvariable=self.var_searchtxt, font=("goudy old style",15,"bold"),bg="lightyellow").place(x=800,y=80,width=165)
        btn_search =Button(self.root, text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=980,y=79,width=100,height=30)
        ###====tittle
        
        title=Label(self.root,text="Supplier Category",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=10,width=1000,height=40)
        
        ######=======Content
        
        #===row 1
        
        lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy old style",15),bg="white").place(x=50,y=80)
  
        txt_supplier_invoice=Entry(self.root,textvariable= self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=160,y=80,width=180)
       
        
        #===Row2
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=120)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=160,y=120,width=180)
      
        
        #===row 3
        
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=160,y=160,width=180)

    #===row 4
        
        lbl_des=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=200)
        self.txt_des=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_des.place(x=160,y=200, width=470,height=120)
        #=== Button
        btn_add = Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",cursor="hand2").place(x=180, y=370,width=110,height=35) 
        btn_update = Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",cursor="hand2").place(x=300, y=370,width=110,height=35) 
        btn_delete= Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",cursor="hand2").place(x=420, y=370,width=110,height=35) 
        btn_clear = Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",cursor="hand2").place(x=540, y=370,width=110,height=35) 
      
      
      #===== Supplier Details
      
        emp_frame =Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place (x=680,y=120,width=410,height=380)
        
        scrolly =Scrollbar(emp_frame,orient=VERTICAL)
        scrollx =Scrollbar(emp_frame,orient=HORIZONTAL)
        
        
        self.supplierTable = ttk.Treeview(emp_frame, column=("invoice", "name", "contact", "des"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.xview)
        
        self.supplierTable.heading("invoice",text="Invoice No")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("contact",text="Contact")
        self.supplierTable.heading("des",text="Description")

        self.supplierTable["show"]="headings"
        
        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("contact",width=100)
        self.supplierTable.column("des",width=100)
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #============================
     
    def add(self):
        con = sqlite3.connect(database=r'qtc.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row= cur.fetchone()
                if row !=None:
                    messagebox.showerror("Error ","This Invoice No already assigned, try diffrient",parent=self.root)
                else:
                    cur.execute("insert into supplier(invoice, name, contact, des) values (?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),     
                        self.txt_des.get('1.0',END),
                     
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Suppplier Addedd Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"An error occurred: {str(ex)}",parent= self.root)
            
    def show (self):
            con = sqlite3.connect(database=r'qtc.db')
            cur = con.cursor()
            try:
                cur.execute("Select * from supplier")
                rows= cur.fetchall()
                self.supplierTable.delete(*self.supplierTable.get_children())
                for row in rows :
                    self.supplierTable.insert('',END,values=row)
                    
            except Exception as ex:
             messagebox.showerror("Error", f"An error occurred: {str(ex)}",parent= self.root)
            
    def show (self):
            con = sqlite3.connect(database=r'qtc.db')
            cur = con.cursor()
            try:
                cur.execute("Select * from supplier")
                rows= cur.fetchall()
                self.supplierTable.delete(*self.supplierTable.get_children())
                for row in rows :
                    self.supplierTable.insert('',END,values=row)
                    
            except Exception as ex:
             messagebox.showerror("Error", f"An error occurred: {str(ex)}",parent= self.root)
    def get_data(self,ev):
             f=self.supplierTable.focus()
             content=(self.supplierTable.item(f))
             row = content['values']
             #print(row)
                       
             self.var_sup_invoice.set(row[0])
             self.var_name.set(row[1])      
             self.var_contact.set(row[2])           
             self.txt_des.delete('1.0',END)
             self.txt_des.insert(END,row[3])                    
    def update(self):
        con = sqlite3.connect(database=r'qtc.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice no. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row= cur.fetchone()
                if row ==None:
                    messagebox.showerror("Error ","Invalid Supplier",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,  des=? where invoice=?",(
                    
                        self.var_name.get(),                    
                        self.var_contact.get(),                           
                        self.txt_des.get('1.0',END),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"An error occurred: {str(ex)}",parent= self.root)
            
    def delete(self):
        con = sqlite3.connect(database=r'qtc.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice no. must be required", parent=self.root)
            else:
                
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Supplier ID", parent=self.root)
                else:
                    answer = messagebox.askyesno("Confirmation", "Do you want to delete this Supplier?", parent=self.root)
                    if answer:
                        cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "Supplier Deleted Successfully", parent=self.root)
                        
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"An error occurred: {str(ex)}", parent=self.root)
            
    def clear(self):
             self.var_sup_invoice.set("")
             self.var_name.set("")         
             self.var_contact.set("") 
             self.txt_des.delete('1.0',END)         
             self.var_searchtxt.set("")
             self.show()
             
    def search(self):
        con = sqlite3.connect(database=r'qtc.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Invoice no.  should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=? ", ( self.var_searchtxt.get(),))
                rows = cur.fetchall()
                if rows:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    for row in rows:
                        self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"An error occurred: {str(ex)}", parent=self.root)

                   
if __name__ == "__main__":
    root = Tk()
    obj =  supplierClass(root)
    root.mainloop()


