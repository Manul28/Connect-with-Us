import socket
import tkinter as tk
from tkinter import *
from tkinter import ttk
import threading
import datetime
from tkinter.ttk import Style
import requests
import customtkinter
import tkinter.messagebox as tkmb
import subprocess
from pyngrok import ngrok
import sqlite3
from PIL import ImageTk

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("DRDO Login Page")
root.geometry("550x550")
icon_path = "images/iconimage.ico"
root.iconbitmap(icon_path)
label = customtkinter.CTkLabel(
    root, text="Inter-Lab Login System", font=("Roboto", 18))
label.pack(pady=20)

LOG_FILENAME = "file_send_log.txt"
LOG_FILENAME2 = "file_recieve_log.txt"


def authenticate(username, password):
    conn = sqlite3.connect('user_credentials.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT password FROM users WHERE username = ?', (username,))
    stored_password = cursor.fetchone()

    conn.close()

    if stored_password is None:
        return False
    return stored_password[0] == password


def gui_sender():
    def get_public_ip():
        try:
            response = requests.get("https://api64.ipify.org?format=json")
            data = response.json()
            return data["ip"]
        except Exception as e:
            print(f"Error getting public IP: {e}")
            return None

    def get_geolocation(ip_address):
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        location = data.get("city", "Unknown")
        return location

    def send_file(filename, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            print(f"Waiting for a connection on {host}:{port}...")
            client_socket, client_address = server_socket.accept()
            print(f"Connected to: {client_address}")
            with open(filename, "rb") as file:
                data = file.read(1024)
                while data:
                    client_socket.send(data)
                    data = file.read(1024)
            print("File sent successfully.")
            log_entry = f"{filename} sent to {host} at {datetime.datetime.now()}"
            ip_address = get_public_ip()
            if ip_address:
                location = get_geolocation(ip_address)

            log_entry += f" from {location}\n"
            with open(LOG_FILENAME, "a") as log_file:
                log_file.write(log_entry)

    def send_button_clicked():
        filename = file_entry.get()
        host = '127.0.0.1'
        port = 4900
        threading.Thread(target=send_file, args=(filename, host, port)).start()

    root1 = tk.Tk()
    root1.title("File Sender GUI")
    root1.iconbitmap(icon_path)
    file_label = tk.Label(root1, text="File to Send:")
    file_entry = tk.Entry(root1)
    send_button = customtkinter.CTkButton(
        root1, text="Send File", command=send_button_clicked)
    send_button.pack(pady=10, padx=12)
    logout_button = customtkinter.CTkButton(
        root1, text="Logout", fg_color="blue", command=quit)
    logout_button.pack(pady=12, padx=10)

    file_label.pack()
    file_entry.pack()
    send_button.pack()
    logout_button.pack()

    # Start the GUI event loop
    heading = Label(root1, text="INMAS FILE TRANSFER GUI", font=(
        "Microsoft Yahei UI Light", 9, "bold"), bg='white')
    heading.place(x=5, y=5)

    root1.geometry("600x550")
    root1.mainloop()


def gui_reciever():
    def get_public_ip():
        try:
            response = requests.get("https://api64.ipify.org?format=json")
            data = response.json()
            return data["ip"]
        except Exception as e:
            print(f"Error getting public IP: {e}")
            return None

    def get_geolocation(ip_address):
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()
        location = data.get("city", "Unknown")
        return location

    def receive_file(save_as, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))

            with open(save_as, "wb") as file:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    file.write(data)
            log_entry = f"{save_as} received from {host} at {datetime.datetime.now()}"
            log_entry2 = f""
            ip_address = get_public_ip()
            if ip_address:
                location = get_geolocation(ip_address)
                log_entry = f"{save_as} received from {host} at {datetime.datetime.now()} from {location}\n"
                log_entry2 = f" target is {location}\n"
            else:
                log_entry = f"{save_as} received from {host} at {datetime.datetime.now()} from Unknown\n"
            with open(LOG_FILENAME2, "a") as log_file:
                log_file.write(log_entry)
            with open(LOG_FILENAME, "a") as log_file:
                log_file.write(log_entry2)
            print("File received successfully.")

    def receive_button_clicked():
        save_as = save_as_entry.get()
        tunnel = ngrok.connect(4900, "tcp")
        tunnel_url = tunnel.public_url
        parts = tunnel_url.split(":")
        forwarded_port = int(parts[-1])
        forwarded_host = parts[1][2:]
        ip_address = socket.gethostbyname(forwarded_host)
        threading.Thread(target=receive_file, args=(
            save_as, ip_address, forwarded_port)).start()


# Create the main application window
    root5 = tk.Tk()
    root5.title("File Receiver GUI")
# Create and place GUI widgets
    save_as_label = tk.Label(root5, text="Save As:")
    save_as_entry = tk.Entry(root5)
    receive_button = customtkinter.CTkButton(
        root5, text="Receive File", command=receive_button_clicked)
    receive_button.pack(pady=10, padx=12)
    logout_button = customtkinter.CTkButton(
        root5, text="Logout", fg_color="blue", command=quit)
    logout_button.pack(pady=12, padx=10)

    save_as_label.pack()
    save_as_entry.pack()
    receive_button.pack()
    logout_button.pack()

# Start the GUI event loop
    heading = Label(root5, text="INMAS FILE TRANSFER GUI", font=(
        "Microsoft Yahei UI Light", 9, "bold"), bg='white')
    heading.place(x=5, y=5)

    root5.geometry("500x450")
    root5.mainloop()


def gui_chat_sender_thread():
    subprocess.run(["py", "chat_client.py"], shell=True)


def gui_chat_reciever_thread():
    subprocess.run(["py", "chat_client_2.py"], shell=True)


def gui_chat_sender():
    server_thread = threading.Thread(target=gui_chat_sender_thread)
    server_thread.start()
    server_thread.join()


def gui_chat_reciever():
    server_thread = threading.Thread(target=gui_chat_reciever_thread)
    server_thread.start()
    server_thread.join()


def choice():
    root4 = tk.Tk()
    root4.title("DRDO Login Page")
    root4.geometry("550x550")
    icon_path = "images/iconimage.ico"
    root4.iconbitmap(icon_path)
    sender_button = customtkinter.CTkButton(
        root4, text="Sender", fg_color="blue", command=gui_sender)
    sender_button.pack(pady=12, padx=10)
    reciever_button = customtkinter.CTkButton(
        root4, text="Reciever", fg_color="blue", command=gui_reciever)
    reciever_button.pack(pady=12, padx=10)
    chat1_button = customtkinter.CTkButton(
        root4, text="Chat as Client-Sender", fg_color="blue", command=gui_chat_sender)
    chat1_button.pack(pady=12, padx=10)
    chat2_button = customtkinter.CTkButton(
        root4, text="Chat as Client-Reciever", fg_color="blue", command=gui_chat_reciever)
    chat2_button.pack(pady=12, padx=10)
    logout_button = customtkinter.CTkButton(
        root4, text="Logout", fg_color="blue", command=quit)
    logout_button.pack(pady=12, padx=10)


def inventory_thread():
    subprocess.run(["py", "inventory.py"], shell=True)


def inventory():
    server_thread = threading.Thread(target=inventory_thread)
    server_thread.start()
    server_thread.join()


def add_user():
    subprocess.run(["py", "add_user.py"], shell=True)


def login():
    new_window = customtkinter.CTkToplevel(root)

    new_window.title("Logged-In")

    new_window.geometry("350x150")

    if authenticate(user_entry.get(), user_pass.get()):
        tkmb.showinfo(title="Login Successful",
                      message="You have logged in Successfully")
        customtkinter.CTkLabel(new_window, text="Access Given").pack()
        root2 = customtkinter.CTk()
        root2.geometry("450x550")
        icon_path = "images/iconimage.ico"
        root2.iconbitmap(icon_path)

        def entry_update(text):
            entry.delete(0, END)
            entry.insert(0, text)

        def choice_2():
            selected = entry.get()
            if not selected:
                tkmb.showerror(title="Lab Selection Error",
                               message="Please select a lab before proceeding.")
            else:
                choice()
        entry = Entry(root2, width=30, font=(
            "Microsoft Yahei UI Light", 9, "bold"), bg="white")
        entry.pack(padx=10, pady=25)
        button_dict = {}
        option = ["Mangalore DRDO", "Chennai DRDO",
                  "Manipur College Lab", "INMAS DRDO"]
        for i in option:
            def func(x=i):
                return entry_update(x)
            root2.title("INMAS DRDO")
            button_dict[i] = customtkinter.CTkButton(
                root2, width=40, text=i, fg_color="blue", command=func)
            button_dict[i].pack()
        heading = Label(root2, text="Select The Lab To Communicate", font=(
            "Microsoft Yahei UI Light", 9, "bold"), bg='white')
        heading.place(x=175, y=46)
        proceed_button = customtkinter.CTkButton(
            root2, text="Proceed", command=choice_2)
        proceed_button.pack(pady=12, padx=10)
        inv_button = customtkinter.CTkButton(
            root2, text="Inventory", command=inventory)
        inv_button.pack(pady=12, padx=10)
        logout_button = customtkinter.CTkButton(
            root2, text="Logout", fg_color="blue", command=quit)
        logout_button.pack(pady=12, padx=10)
        root2.mainloop()

    else:
        tkmb.showerror(title="Login Failed",
                       message="Invalid Username or Password")


def show():
    hide_button = Button(root, image=hide_image, command=hide,
                         relief=FLAT, activebackground="white", bd=0, background='white', height=20, width=30)
    hide_button.place(x=480, y=260)
    user_pass.configure(show='')


def hide():
    show_button = Button(root, image=show_image, command=show,
                         relief=FLAT, activebackground='white', bd=0, background='white', height=20, width=30)
    show_button.place(x=480, y=260)
    user_pass.configure(show='*')


show_image = ImageTk.PhotoImage(file='images\\open_eye.jpg')
hide_image = ImageTk.PhotoImage(file='images\\close_eye.jpg')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(
    master=frame, text="SIGN-IN", font=("Roboto", 22))
label.pack(pady=12, padx=10)

user_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = customtkinter.CTkEntry(
    master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)
show_button = Button(root, image=show_image, command=show,
                     relief=FLAT, activebackground='white', bd=0, background='white', height=20, width=30)
show_button.place(x=480, y=260)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

addbutton = customtkinter.CTkButton(
    master=frame, text="Add User", fg_color="blue", command=add_user)
addbutton.pack(pady=12, padx=10)


root.geometry("620x550")
root.mainloop()
