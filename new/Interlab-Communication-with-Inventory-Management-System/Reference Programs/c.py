# import socket
# import tkinter as tk
# from tkinter import filedialog

# def receive_file(save_as, host, port):
#     # Your receive_file function code ...
#      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect((host, port))
#         with open(save_as, "wb") as file:
#             while True:
#                 data = client_socket.recv(1024)
#                 if not data:
#                     break
#                 file.write(data)
#         print("File received successfully.")

# def receive_button_clicked():
#     save_as = filedialog.asksaveasfilename(title="Save received file as")
#     if save_as:
#         host = entry_host.get()
#         port = int(entry_port.get())
#         receive_file(save_as, host, port)

# # Create the main application window
# root = tk.Tk()
# root.title("File Receiver GUI")

# # Create and place GUI widgets
# label_host = tk.Label(root, text="Host:")
# entry_host = tk.Entry(root)
# label_port = tk.Label(root, text="Port:")
# entry_port = tk.Entry(root)
# button_receive = tk.Button(root, text="Receive File", command=receive_button_clicked)

# label_host.pack()
# entry_host.pack()
# label_port.pack()
# entry_port.pack()
# button_receive.pack()

# # Start the GUI event loop
# root.mainloop()


# -----------------------------------------------------------------------------------------------------






import socket
import tkinter as tk
from tkinter import filedialog
import threading
import datetime
import requests

LOG_FILENAME = "file_receive_log.txt"
LOG_FILENAME2 = "file_send_log.txt"

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
        log_entry2=f""
        ip_address = get_public_ip()
        if ip_address:
                    location = get_geolocation(ip_address)
                    log_entry = f"{save_as} received from {host} at {datetime.datetime.now()} from {location}\n"
                    log_entry2 = f" target is {location}\n"
        else:
                    log_entry = f"{save_as} received from {host} at {datetime.datetime.now()} from Unknown\n"
        with open(LOG_FILENAME, "a") as log_file:
            log_file.write(log_entry)
        with open(LOG_FILENAME2, "a") as log_file:
             log_file.write(log_entry2)
        print("File received successfully.")


def receive_button_clicked():
    save_as = save_as_entry.get()
    host = host_entry.get()
    port = int(port_entry.get())
    threading.Thread(target=receive_file, args=(save_as, host, port)).start()


# Create the main application window
root = tk.Tk()
root.title("File Receiver GUI")

# Create and place GUI widgets
save_as_label = tk.Label(root, text="Save As:")
save_as_entry = tk.Entry(root)
host_label = tk.Label(root, text="Host:")
host_entry = tk.Entry(root)
port_label = tk.Label(root, text="Port:")
port_entry = tk.Entry(root)
receive_button = tk.Button(root, text="Receive File",command=receive_button_clicked)

save_as_label.pack()
save_as_entry.pack()
host_label.pack()
host_entry.pack()
port_label.pack()
port_entry.pack()
receive_button.pack()

# Start the GUI event loop
heading=Label(root,text="INMAS FILE TRANSFER GUI",font=("Microsoft Yahei UI Light",9,"bold"),bg='white')
heading.place(x=5,y=5)

root.geometry("500x450")
root.mainloop()























# import socket
# import tkinter as tk
# from tkinter import filedialog
# import threading
# import datetime

# LOG_FILENAME = "file_receive_log.txt"

# def receive_file(save_as, host, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect((host, port))

#         with open(save_as, "wb") as file:
#             while True:
#                 data = client_socket.recv(1024)
#                 if not data:
#                     break
#                 file.write(data)

#         log_entry = f"{save_as} received from {host} at {datetime.datetime.now()}\n"
#         with open(LOG_FILENAME, "a") as log_file:
#             log_file.write(log_entry)

#         print("File received successfully.")

# def receive_button_clicked():
#     save_as = save_as_entry.get()
#     host = host_entry.get()
#     port = int(port_entry.get())
#     threading.Thread(target=receive_file, args=(save_as, host, port)).start()

# # Create the main application window
# root = tk.Tk()
# root.title("File Receiver GUI")

# # Create and place GUI widgets
# save_as_label = tk.Label(root, text="Save As:")
# save_as_entry = tk.Entry(root)
# host_label = tk.Label(root, text="Host:")
# host_entry = tk.Entry(root)
# port_label = tk.Label(root, text="Port:")
# port_entry = tk.Entry(root)
# receive_button = tk.Button(root, text="Receive File", command=receive_button_clicked)

# save_as_label.pack()
# save_as_entry.pack()
# host_label.pack()
# host_entry.pack()
# port_label.pack()
# port_entry.pack()
# receive_button.pack()

# # Start the GUI event loop
# root.mainloop()
