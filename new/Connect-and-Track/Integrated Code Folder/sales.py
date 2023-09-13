from tkinter import *
# from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os
import pandas as pd
from tkinter import filedialog
import xlrd
from tabulate import tabulate
import tkinter.font as tkFont


class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        icon_path = "images/iconimage.ico"
        self.root.iconbitmap(icon_path)
        self.root.title("Inventory Management System | INMAS DRDO")
        self.root.config(bg="white")
        self.root.focus_force()
        self.bill_list = []
        self.zoom_factor = 1.0
        self.var_invoice = StringVar()
        # ====title====
        lb1_title = Label(self.root, text="Records ", font=("goudy old style", 30),
                          bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)

        lb1_invoice = Label(self.root, text="Invoice No.", font=(
            "times new roman", 15), bg="white").place(x=50, y=100)

        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=(
            "times new roman", 15), bg="white").place(x=160, y=100, width=180, height=28)

        btn_search = Button(self.root, text="Search", command=self.search, font=("time new roman", 15, "bold"),
                            bg="#2196f3", fg="white", cursor="hand2").place(x=330, y=100, width=120, height=28)

        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("time new roman", 15, "bold"),
                           bg="lightgray", cursor="hand2").place(x=440, y=100, width=120, height=28)

        btn_add = Button(self.root, text="Add", command=self.add, font=("time new roman", 15, "bold"),
                         bg="lightgray", cursor="hand2").place(x=560, y=100, width=90, height=28)
        btn_open_excel = Button(self.root, text="Open Excel", command=self.open_excel, font=("time new roman", 15, "bold"),
                                bg="lightgray", cursor="hand2").place(x=920, y=450, width=150, height=28)

        btn_save = Button(self.root, text="Save", command=self.save_changes, font=("time new roman", 15, "bold"),
                          bg="lightgray", cursor="hand2").place(x=700, y=450, width=90, height=28)
        btn_delete = Button(self.root, text="Delete", command=self.delete_record, font=("time new roman", 15, "bold"),
                            bg="lightgray", cursor="hand2").place(x=800, y=450, width=110, height=28)
        btn_zoomin = Button(self.root, text="+", command=self.zoom_in, font=("time new roman", 15, "bold"),
                            bg="lightgray", cursor="hand2").place(x=660, y=100, width=20, height=28)
        btn_zoomout = Button(self.root, text="-", command=self.zoom_out, font=("time new roman", 15, "bold"),
                             bg="lightgray", cursor="hand2").place(x=680, y=100, width=20, height=28)

        # ===Bill List===
        sales_Frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_Frame.place(x=50, y=140, width=120, height=330)

        scrolly = Scrollbar(sales_Frame, orient=VERTICAL)
        self.sales_list = Listbox(sales_Frame, font=(
            "goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview)
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind("<ButtonRelease-1>", self.get_data)

        # Bill Area======
        bill_Frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_Frame.place(x=150, y=140, width=530, height=330)

        lb1_title2 = Label(bill_Frame, text="Record Area", font=(
            "goudy old style", 20), bg="orange").pack(side=TOP, fill=X)

        scrolly2 = Scrollbar(bill_Frame, orient=VERTICAL)
        self.bill_area = Text(bill_Frame, font=(
            "goudy old style", 15), bg="lightyellow", yscrollcommand=scrolly2.set, wrap=NONE)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.bill_area.yview)

        scrolly3 = Scrollbar(bill_Frame, orient=HORIZONTAL)
        self.bill_area = Text(bill_Frame, font=(
            "goudy old style", 15), bg="lightyellow", xscrollcommand=scrolly3.set, wrap=NONE)
        scrolly3.pack(side=BOTTOM, fill=X)
        scrolly3.config(command=self.bill_area.xview)
        self.bill_area.pack(fill=BOTH, expand=1)

        # Image========
        self.bill_photo = Image.open("images/cat2.jpg")
        self.bill_photo = self.bill_photo.resize((450, 300), Image.ANTIALIAS)
        self.bill_photo = ImageTk.PhotoImage(self.bill_photo)

        lb1_image = Label(self.root, image=self.bill_photo, bd=0)
        lb1_image.place(x=700, y=110)

        self.show()

    def update_font_size(self):
        font_size = 10 + int(4 * self.zoom_factor)
        self.bill_area.config(font=("goudy old style", font_size))

    def zoom_in(self):
        self.zoom_factor += 0.1
        self.update_font_size()

    def zoom_out(self):
        self.zoom_factor -= 0.1
        self.update_font_size()

    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0, END)
        for i in os.listdir('record'):
            if i.split('.')[-1] == 'txt':
                self.sales_list.insert(END, i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self, ev):
        row = self.sales_list.curselection()
        file_name = self.sales_list.get(row)
        # Set the invoice number in the Entry widget
        self.var_invoice.set(file_name.split('.')[0])
        self.bill_area.delete('1.0', END)
        with open(f'record/{file_name}', 'r') as fp:
            for i in fp:
                self.bill_area.insert(END, i)

    def search(self):
        if self.var_invoice.get() == "":
            messagebox.showerror(
                "Error", "Invoice should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp = open(f'record/{self.var_invoice.get()}.txt')
                self.bill_area.delete('1.0', END)
                for i in fp:
                    self.bill_area.insert(END, i)
                fp.close()
            else:
                messagebox.showerror(
                    "Error", "Invalid Invoice Invalid", parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0', END)

    def add(self):
        invoice_number = self.var_invoice.get()
        if invoice_number == "":
            messagebox.showerror(
                "Error", "Invoice should be required", parent=self.root)
        else:
            file_name = f'record/{invoice_number}.txt'
            try:
                with open(file_name, 'w') as fp:
                    # Retrieve all text from the Text widget
                    contents = self.bill_area.get('1.0', END)
                    fp.write(contents)
                self.show()
                self.var_invoice.set("")  # Clear the invoice field
                self.bill_area.delete('1.0', END)  # Clear the bill_area widget
                messagebox.showinfo(
                    "Success", "File created and saved successfully", parent=self.root)
                self.show()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"An error occurred: {str(e)}", parent=self.root)

    def save_changes(self):
        invoice_number = self.var_invoice.get()
        if invoice_number == "":
            messagebox.showerror(
                "Error", "Invoice should be required", parent=self.root)
        else:
            file_name = f'record/{invoice_number}.txt'
            try:
                with open(file_name, 'w') as fp:
                    # Retrieve all text from the Text widget
                    contents = self.bill_area.get('1.0', END)
                    fp.write(contents)
                messagebox.showinfo(
                    "Success", "Changes saved successfully", parent=self.root)
            except Exception as e:
                messagebox.showerror(
                    "Error", f"An error occurred: {str(e)}", parent=self.root)

    def delete_record(self):
        invoice_number = self.var_invoice.get()
        if invoice_number == "":
            messagebox.showerror(
                "Error", "Invoice should be required", parent=self.root)
        else:
            file_name = f'record/{invoice_number}.txt'
            if os.path.exists(file_name):
                try:
                    os.remove(file_name)
                    self.show()  # Refresh the list after deletion
                    self.var_invoice.set("")  # Clear the invoice field
                    # Clear the bill_area widget
                    self.bill_area.delete('1.0', END)
                    messagebox.showinfo(
                        "Success", "Record deleted successfully", parent=self.root)
                except Exception as e:
                    messagebox.showerror(
                        "Error", f"An error occurred: {str(e)}", parent=self.root)
            else:
                messagebox.showerror(
                    "Error", "Record does not exist", parent=self.root)

    def open_excel(self):
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(), filetypes=[("Excel Files", "*.xlsx")])

        if file_path:
            self.display_excel_data(file_path)
            self.var_invoice.set(os.path.basename(file_path).split('.')[0])

    def display_excel_data(self, file_path):
        self.bill_area.delete('1.0', END)
        try:
            excel_data = pd.read_excel(file_path, engine='openpyxl')

            if excel_data.empty:
                messagebox.showwarning(
                    "Empty Excel File", "The selected Excel file is empty.", parent=self.root)
            else:
                font_size = 5
                width = 50  # Adjust as needed
                height = 15  # Adjust as needed
                table = tabulate(excel_data, headers='keys', tablefmt='grid')
                font = tkFont.Font(family="Courier", size=font_size)
                self.bill_area.config(font=font)
                self.bill_area.insert(END, table)
                self.bill_area.config(width=width, height=height)
        except Exception as e:
            messagebox.showerror(
                "Error", f"An error occurred while opening the Excel file: {str(e)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
