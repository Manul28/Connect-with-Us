# import socket
# import tkinter as tk
# from tkinter import filedialog


# def send_file(filename, host, port):
#     # Your send_file function code ...
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host, port))
#         server_socket.listen()
#         print(f"Waiting for a connection on {host}:{port}...")
#         client_socket, client_address = server_socket.accept()
#         print(f"Connected to: {client_address}")
#         with open(filename, "rb") as file:
#             data = file.read(1024)
#             while data:
#                  client_socket.send(data)
#                  data = file.read(1024)
#         print("File sent successfully.")


# def send_button_clicked():
#     filename = filedialog.askopenfilename(title="Select a file to send")
#     if filename:
#         host = entry_host.get()
#         port = int(entry_port.get())
#         send_file(filename, host, port)


# # Create the main application window
# root = tk.Tk()
# root.title("File Sender GUI")

# # Create and place GUI widgets
# label_host = tk.Label(root, text="Host:")
# entry_host = tk.Entry(root)
# label_port = tk.Label(root, text="Port:")
# entry_port = tk.Entry(root)
# button_send = tk.Button(root, text="Send File", command=send_button_clicked)

# label_host.pack()
# entry_host.pack()
# label_port.pack()
# entry_port.pack()
# button_send.pack()

# # Start the GUI event loop
# root.mainloop()

# import socket
# import tkinter as tk
# from tkinter import filedialog
# import threading

# def send_file(filename, host, port):
#     # Your send_file function code ...
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host, port))
#         server_socket.listen()
#         print(f"Waiting for a connection on {host}:{port}...")
#         client_socket, client_address = server_socket.accept()
#         print(f"Connected to: {client_address}")
#         with open(filename, "rb") as file:
#             data = file.read(1024)
#             while data:
#                  client_socket.send(data)
#                  data = file.read(1024)
#         print("File sent successfully.")

# def send_button_clicked():
#     filename = filedialog.askopenfilename(title="Select a file to send")
#     if filename:
#         host = entry_host.get()
#         port = int(entry_port.get())
#         threading.Thread(target=send_file, args=(filename, host, port)).start()

# # Create the main application window
# root = tk.Tk()
# root.title("File Sender GUI")

# # Create and place GUI widgets
# label_host = tk.Label(root, text="Host:")
# entry_host = tk.Entry(root)
# label_port = tk.Label(root, text="Port:")
# entry_port = tk.Entry(root)
# button_send = tk.Button(root, text="Send File", command=send_button_clicked)

# label_host.pack()
# entry_host.pack()
# label_port.pack()
# entry_port.pack()
# button_send.pack()

# # Start the GUI event loop
# root.mainloop()

# -----------------------------------------------------------------------------------------------------------
# import socket
# def send_file(filename, host, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
#         server_socket.bind((host, port))
#         server_socket.listen()
#         print(f"Waiting for a connection on {host}:{port}...")
#         client_socket, client_address = server_socket.accept()
#         print(f"Connected to: {client_address}")
#         with open(filename, "rb") as file:
#             data = file.read(1024)
#             while data:
#                 client_socket.send(data)
#                 data = file.read(1024)
#                 print("File sent successfully.")

# if __name__ == "__main__":
#     host = "127.0.0.1" # Change this to the server's IP address
#     port = 4656   # Choose a port number
#     filename = "file_to_send.txt" # Change this to the filename you want to send
#     send_file(filename, host, port)

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------










import socket
import tkinter as tk
from tkinter import filedialog
import threading
import datetime
import requests

LOG_FILENAME = "file_send_log.txt"


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


# Create the main application window
root = tk.Tk()
root.title("File Sender GUI")

# Create and place GUI widgets
file_label = tk.Label(root, text="File to Send:")
file_entry = tk.Entry(root)
host_label = tk.Label(root, text="Host:")
host_entry = tk.Entry(root)
port_label = tk.Label(root, text="Port:")
port_entry = tk.Entry(root)
send_button = tk.Button(root, text="Send File", command=send_button_clicked)

file_label.pack()
file_entry.pack()
host_label.pack()
host_entry.pack()
port_label.pack()
port_entry.pack()
send_button.pack()

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

# LOG_FILENAME = "file_send_log.txt"


# def send_file(filename, host, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
#         client_socket.connect((host, port))
#         with open(filename, "rb") as file:
#             data = file.read(1024)
#             while data:
#                 client_socket.send(data)
#                 data = file.read(1024)

#         log_entry = f"{filename} sent to {host} at {datetime.datetime.now()}\n"
#         with open(LOG_FILENAME, "a") as log_file:
#             log_file.write(log_entry)

#         print("File sent successfully.")


# def send_button_clicked():
#     filename = file_entry.get()
#     host = host_entry.get()
#     port = int(port_entry.get())
#     threading.Thread(target=send_file, args=(filename, host, port)).start()


# # Create the main application window
# root = tk.Tk()
# root.title("File Sender GUI")

# # Create and place GUI widgets
# file_label = tk.Label(root, text="File to Send:")
# file_entry = tk.Entry(root)
# host_label = tk.Label(root, text="Host:")
# host_entry = tk.Entry(root)
# port_label = tk.Label(root, text="Port:")
# port_entry = tk.Entry(root)
# send_button = tk.Button(root, text="Send File", command=send_button_clicked)

# file_label.pack()
# file_entry.pack()
# host_label.pack()
# host_entry.pack()
# port_label.pack()
# port_entry.pack()
# send_button.pack()

# # Start the GUI event loop
# root.mainloop()
