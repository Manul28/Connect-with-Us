from tkinter import *
# from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
from win10toast import ToastNotifier


class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | INMAS DRDO")
        self.root.config(bg="white")
        self.root.focus_force()
        # ==========================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_pid = StringVar()
        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.cat_list = []
        self.sup_list = []
        self.fetch_cat_sup()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()
        # self.var_cat=StringVar()

        product_Frame = Frame(self.root, bd=3, relief=RIDGE)
        product_Frame.place(x=10, y=10, width=450, height=480)

        # =====title====
        title = Label(product_Frame, text="Manage product Details", font=(
            "goudy old style", 18), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        lb1_category = Label(product_Frame, text="Category", font=(
            "goudy old style", 18), bg="white").place(x=30, y=60)
        lb1_supplier = Label(product_Frame, text="Supplier", font=(
            "goudy old style", 18), bg="white").place(x=30, y=110)
        lb1_product_name = Label(product_Frame, text="Name", font=(
            "goudy old style", 18), bg="white").place(x=30, y=160)
        lb1_price = Label(product_Frame, text="Price", font=(
            "goudy old style", 18), bg="white").place(x=30, y=210)
        lb1_qty = Label(product_Frame, text="Quantity", font=(
            "goudy old style", 18), bg="white").place(x=30, y=260)
        lb1_status = Label(product_Frame, text="Status", font=(
            "goudy old style", 18), bg="white").place(x=30, y=310)

        # txt_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=30,y=60)
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.var_cat, values=self.cat_list,
                               state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.var_sup, values=self.sup_list,
                               state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_sup.place(x=150, y=110, width=200)
        cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=(
            "goudy old style", 15), bg='lightyellow').place(x=150, y=160, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=(
            "goudy old style", 15), bg='lightyellow').place(x=150, y=210, width=200)
        txt_status = Entry(product_Frame, textvariable=self.var_qty, font=(
            "goudy old style", 15), bg='lightyellow').place(x=150, y=260, width=200)
        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=(
            "Active", "Inactive"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        # button
        btn_add = Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15),
                         bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=400, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=("goudy old style", 15),
                            bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=400, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete, font=("goudy old style", 15),
                            bg="#f44336", fg="white", cursor="hand2").place(x=230, y=400, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=("goudy old style", 15),
                           bg="#607d8b", fg="white", cursor="hand2").place(x=340, y=400, width=100, height=40)
        # searchFrame
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=(
            "goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=480, y=10, width=600, height=80)

        # option
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=(
            "Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=(
            "goudy old style", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search", font=("goudy old style", 15),
                            bg="#4caf50", fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

        # Product Details

        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product__table = ttk.Treeview(p_frame, columns=(
            "pid", "Category", "Supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product__table.xview)
        scrolly.config(command=self.product__table.yview)

        self.product__table.heading("pid", text="P ID")
        self.product__table.heading("Category", text="Category")
        self.product__table.heading("Supplier", text="Supplier")
        self.product__table.heading("name", text="Name")
        self.product__table.heading("price", text="Price")
        self.product__table.heading("qty", text="Quantity")
        self.product__table.heading("status", text="status")

        self.product__table["show"] = "headings"
        self.product__table.column("pid", width=90)
        self.product__table.column("Category", width=100)
        self.product__table.column("Supplier", width=100)
        self.product__table.column("name", width=100)
        self.product__table.column("price", width=100)
        self.product__table.column("qty", width=100)
        self.product__table.column("status", width=100)
        self.product__table.pack(fill=BOTH, expand=1)
        self.product__table.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        self.check_product_quantity()
    # =====================================================

    def check_product_quantity(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute(
                "SELECT name, qty FROM product WHERE CAST(qty as INTEGER) < 10")
            low_quantity_products = cur.fetchall()
            for product in low_quantity_products:
                product_name, quantity = product
                message = f"Low quantity alert: {product_name} has only {quantity} left."
                messagebox.showinfo(
                    "Alert", message, parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error checking product quantity: {str(ex)}", parent=self.root)

    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select name from category")
            cat = cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat) > 0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            cur.execute("Select name from supplier")
            sup = cur.fetchall()
            self.sup_list.append("Empty")
            if len(sup) > 0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat.get() == "Select" or self.var_cat.get() == "Empty" or self.var_sup.get() == "Select" or self.var_name.get() == "":
                messagebox.showerror(
                    "Error", f"All fields Must be required:", parent=self.root)
            else:
                cur.execute("Select *from product where name=?",
                            (self.var_name.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror(
                        "Error", "This Category is already assigned,try any different category", parent=self.root)
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get()
                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Product Added Successfully", parent=self.root)
                    if int(self.var_qty.get()) < 10:
                        self.check_product_quantity()
                        self.show()
                    else:
                        self.show()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows = cur.fetchall()
            self.product__table.delete(*self.product__table.get_children())
            for row in rows:
                if int(row[5]) < 10:
                    self.product__table.insert(
                        '', END, values=row, tags=("red_row",))
                else:
                    self.product__table.insert(
                        '', END, values=row, tags=("green_row",))
            self.product__table.tag_configure(
                "red_row", background="red", foreground="white")
            self.product__table.tag_configure(
                "green_row", background="green", foreground="white")

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.product__table.focus()
        content = (self.product__table.item(f))
        row = content['values']
        print(row)
        self.var_pid.set(row[0])
        self.var_cat.set(row[1])
        self.var_sup.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "Error", f"Product ID Must be required:", parent=self.root)
            else:
                cur.execute("Select *from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Product ID", parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?", (
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                        self.var_pid.get()

                    ))
                    con.commit()
                    messagebox.showinfo(
                        "Success", "Product Updated Successfully", parent=self.root)
                    if int(self.var_qty.get()) < 10:
                        self.check_product_quantity()
                        self.show()
                    else:
                        self.show()
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_pid.get() == "":
                messagebox.showerror(
                    "Error", f"Product ID Must be required:", parent=self.root)
            else:
                cur.execute("Select *from product where pid=?",
                            (self.var_pid.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid Product ID", parent=self.root)
                else:
                    op = messagebox.askyesno(
                        "Confirm", "Do you really want to delete this product information?", parent=self.root)
                    if op == True:
                        cur.execute("delete from product where pid=?",
                                    (self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo(
                            "Delete", "Product Successfully deleted", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_pid.set("")
        self.var_cat.set("")
        self.var_sup.set("")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_searchby.set("Select")
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror(
                    "Error", "Select Search option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror(
                    "Error", "Search input should be required ", parent=self.root)
            else:
                cur.execute("select * from employee where " +
                            self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product__table.delete(
                        *self.product__table.get_children())
                    for row in rows:
                        self.product__table.insert('', END, values=row)
                else:
                    messagebox.showerror(
                        "Error", "No record found ", parent=self.root)
        except Exception as ex:
            messagebox.showerror(
                "Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
