import sqlite3
import tkinter as tk
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


def add_user_to_db(username, password):
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        messagebox.showinfo("Success", "User added successfully.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")

    conn.close()


def add_user():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        add_user_to_db(username, password)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror(
            "Error", "Please enter both username and password.")


# Create the main application window
root = customtkinter.CTk()
root.title("Add New User")
icon_path = "images/iconimage.ico"
root.iconbitmap(icon_path)
# Labels and entry fields for username and password
customtkinter.CTkLabel(root, text="Username:").pack()
username_entry = customtkinter.CTkEntry(root)
username_entry.pack()

customtkinter.CTkLabel(root, text="Password:").pack()
password_entry = customtkinter.CTkEntry(root, show="*")
password_entry.pack()

# Button to add a new user
add_button = customtkinter.CTkButton(root, text="Add User", command=add_user)
add_button.pack(padx=5, pady=5)
add_button.pack()
root.geometry("300x300")
root.mainloop()
