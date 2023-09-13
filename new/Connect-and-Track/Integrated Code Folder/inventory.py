from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import datetime
import os
import pytz
import sqlite3


class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1650x1000")
        icon_path = "images/iconimage.ico"
        self.root.iconbitmap(icon_path)
        self.root.title("Inventory Management System | INMAS DRDO")
        self.root.config(bg="white")
        # title
        self.icon_title = PhotoImage(file="images/logo2.png")
        title = Label(self.root, text="DRDO Inventory Management System", image=self.icon_title, compound=LEFT, font=(
            "times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0, y=0, relwidth=1, height=70)

        # btn_logout
        btn_logout = Button(self.root, text="Logout", command=self.root.destroy, font=(
            "times new roman", 15, "bold"), bg="yellow").place(x=1100, y=10, height=50, width=150)
        # clock
        self.lb1_clock = Label(self.root, text="", font=(
            "times new roman", 15), bg="#4d636d", fg="white")

        self.lb1_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()

        # Left Menu
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.ANTIALIAS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=545)

        lb1_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lb1_menuLogo.pack(side=TOP, fill=X)

        self.icon_side = PhotoImage(file="images/side.png")
        lb1_menu = Label(LeftMenu, text="Menu", font=(
            "times new roman", 20), bg="#009688").pack(side=TOP, fill=X)
        self.custom_style = ttk.Style()
        self.custom_style.configure("Custom.TButton", font=(
            "times new roman", 20, "bold"), background="white", foreground="black", padding=10, borderwidth=3)
        btn_employee = ttk.Button(LeftMenu, text="Employee", command=self.employee,
                                  image=self.icon_side, compound=LEFT, style="Custom.TButton", cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)

        btn_supplier = ttk.Button(LeftMenu, text=" Supplier", command=self.supplier,
                                  image=self.icon_side, compound=LEFT, style="Custom.TButton", cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)

        btn_category = ttk.Button(LeftMenu, text=" Category", command=self.category,
                                  image=self.icon_side, compound=LEFT, style="Custom.TButton", cursor="hand2")
        btn_category.pack(side=TOP, fill=X)

        btn_product = ttk.Button(LeftMenu, text=" Product", command=self.product,
                                 image=self.icon_side, compound=LEFT, style="Custom.TButton", cursor="hand2")
        btn_product.pack(side=TOP, fill=X)

        btn_sales = ttk.Button(LeftMenu, text="Records", command=self.sales,
                               image=self.icon_side, compound=LEFT, style="Custom.TButton", cursor="hand2")
        btn_sales.pack(side=TOP, fill=X)
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        cur.execute("select count(*) from employee")
        r = cur.fetchone()
        count1 = r[0]
        self.lb1_employee = Label(self.root, text=f"Employee Count \n is :{count1}", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lb1_employee.place(x=300, y=120, height=120, width=300)

        cur.execute("select count(*) from supplier")
        r = cur.fetchone()
        count1 = r[0]
        self.lb1_supplier = Label(self.root, text=f"Supplier Count \n is :{count1}", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lb1_supplier.place(x=1000, y=120, height=120, width=300)

        cur.execute("select count(*) from category")
        r = cur.fetchone()
        count1 = r[0]
        self.lb1_category = Label(self.root, text=f"Category Count \n is :{count1}", bd=5, relief=RIDGE, bg="#009688", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lb1_category.place(x=650, y=120, height=120, width=300)

        cur.execute("select count(*) from product")
        r = cur.fetchone()
        count1 = r[0]
        self.lb1_Product = Label(self.root, text=f"Product Count \n is :{count1}", bd=5, relief=RIDGE, bg="#607d8b", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lb1_Product.place(x=300, y=300, height=120, width=300)

        onlyfiles = next(os.walk('./record'))[2]
        count1 = len(onlyfiles)
        self.lb1_sales = Label(self.root, text=f"Records Count \n is :{count1}", bd=5, relief=RIDGE, bg="#ffc107", fg="white", font=(
            "goudy old style", 20, "bold"))
        self.lb1_sales.place(x=650, y=300, height=120, width=300)

        # footer
        lb1_clock = Label(self.root, text="DRDO-Inventory Management System ", font=(
            "times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

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

    def sales(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_clock(self):
        current_time = datetime.datetime.now(pytz.timezone(
            'Asia/Kolkata'))  # Adjust the timezone as needed
        formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
        self.lb1_clock.config(
            text=f"Welcome to Inventory Management System\t\t Date: {formatted_time}")
        self.root.after(1000, self.update_clock)  # Update every 1000


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
