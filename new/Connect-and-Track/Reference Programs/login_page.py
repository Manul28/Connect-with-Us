##################SAMPLE OUTLET#########################
# import customtkinter
# import tkinter.messagebox as tkmb

# customtkinter.set_appearance_mode("light")
# customtkinter.set_default_color_theme("green")

# root=customtkinter.CTk()
# root.title("DRDO Login Page")
# root.geometry("500x450")
 
# label=customtkinter.CTkLabel(root,text="Inter-Lab Login System",font=("Roboto",18))
# label.pack(pady=20) 

# def login():
#     # print("Test")
#     username="Manul"
#     password="@1234"
#     new_window=customtkinter.CTkToplevel(root)
  
#     new_window.title("Logged-In")
  
#     new_window.geometry("350x150")
  
#     if user_entry.get() == username and user_pass.get() == password:
#         tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
#         customtkinter.CTkLabel(new_window,text="Access Given").pack()
#     elif user_entry.get() == username and user_pass.get() != password:
#         tkmb.showwarning(title='Wrong password',message='Please check your password')
#     elif user_entry.get() != username and user_pass.get() == password:
#         tkmb.showwarning(title='Wrong username',message='Please check your username')
#     else:
#         tkmb.showerror(title="Login Failed",message="Invalid Username and password")
 
 
# frame=customtkinter.CTkFrame(master=root)
# frame.pack(pady=20,padx=60,fill="both",expand=True)

# label=customtkinter.CTkLabel(master=frame,text="SIGN-IN",font=("Roboto", 22))  
# label.pack(pady=12,padx=10) 

# user_entry=customtkinter.CTkEntry(master=frame,placeholder_text="Username")
# user_entry.pack(pady=12,padx=10)

# user_pass=customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*")
# user_pass.pack(pady=12,padx=10)

# button=customtkinter.CTkButton(master=frame,text="Login",command=login)
# button.pack(pady=12,padx=10)

# # checkbox=customtkinter.CTkCheckBox(master=frame,text="Secured")
# # checkbox.pack(pady=12,padx=10)
#######USERNAME:Manul
#######PASSWORD:@1234
import socket
import tkinter as tk
from tkinter import *
# from tkinter import filedialog
import threading
import datetime
from tkinter.ttk import Style
import requests
import customtkinter
import tkinter.messagebox as tkmb

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")

root=customtkinter.CTk()
root.title("DRDO Login Page")
root.geometry("550x550")
icon_path = "iconimage.ico"
root.iconbitmap(icon_path)
label=customtkinter.CTkLabel(root,text="Inter-Lab Login System",font=("Roboto",18))
label.pack(pady=20) 

LOG_FILENAME = "file_send_log.txt"
def login():
    # print("Test")
    username="*****"
    password="*****"
    new_window=customtkinter.CTkToplevel(root)
  
    new_window.title("Logged-In")
  
    new_window.geometry("350x150")
  
    if user_entry.get() == username and user_pass.get() == password:
        tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
        customtkinter.CTkLabel(new_window,text="Access Given").pack()

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
            host = host_entry.get()
            port = int(port_entry.get())
            threading.Thread(target=send_file, args=(filename, host, port)).start()
        
        root1 = tk.Tk()
        root1.title("File Sender GUI")
        root1.iconbitmap(icon_path)
        file_label = tk.Label(root1, text="File to Send:")
        file_entry = tk.Entry(root1)
        host_label = tk.Label(root1, text="Host:")
        host_entry = tk.Entry(root1)
        port_label = tk.Label(root1, text="Port:")
        port_entry = tk.Entry(root1)
        send_button=tk.Button(root1, text="Send File", command=send_button_clicked)
        # btn1.grid(row=1,column=3,pady=10,padx=100)

        file_label.pack()
        file_entry.pack()
        host_label.pack()
        host_entry.pack()
        port_label.pack()
        port_entry.pack()
        send_button.pack()

        # Start the GUI event loop
        heading=Label(root1,text="INMAS FILE TRANSFER GUI",font=("Microsoft Yahei UI Light",9,"bold"),bg='white')
        heading.place(x=5,y=5)

        root1.geometry("600x550")
        root1.mainloop()
            
    elif user_entry.get() == username and user_pass.get() != password:
        tkmb.showwarning(title='Wrong password',message='Please check your password')
    elif user_entry.get() != username and user_pass.get() == password:
        tkmb.showwarning(title='Wrong username',message='Please check your username')
    else:
        tkmb.showerror(title="Login Failed",message="Invalid Username and password")


 
frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=customtkinter.CTkLabel(master=frame,text="SIGN-IN",font=("Roboto", 22))  
label.pack(pady=12,padx=10) 

user_entry=customtkinter.CTkEntry(master=frame,placeholder_text="Username")
user_entry.pack(pady=12,padx=10)

user_pass=customtkinter.CTkEntry(master=frame,placeholder_text="Password",show="*")
user_pass.pack(pady=12,padx=10)

button=customtkinter.CTkButton(master=frame,text="Login",command=login)
button.pack(pady=12,padx=10)


checkbox=customtkinter.CTkCheckBox(master=frame,text="Remember Me")
checkbox.pack(pady=12,padx=10)

root.geometry("600x550")
root.mainloop()
# checkbox=customtkinter.CTkCheckBox(master=frame,text="Remember Me")
# checkbox.pack(pady=12,padx=10)

# root.mainloop()
