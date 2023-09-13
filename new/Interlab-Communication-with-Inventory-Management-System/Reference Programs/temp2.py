import socket
import tkinter as tk
from tkinter import filedialog
import threading
from pyngrok import ngrok


def send_file():
    filename = filedialog.askopenfilename(title="Select a file to send")
    if filename:
        threading.Thread(target=send_file_thread, args=(filename,)).start()


def send_file_thread(filename):
    try:
        host = "127.0.0.1"  # Automatically use the localhost IP address
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, 0))  # Bind to any available port
        port = server_socket.getsockname()[1]  # Get the chosen port
        server_socket.listen()
        http_tunnel = ngrok.connect()
        ssh_tunnel = ngrok.connect(port, "tcp")
        status_label.config(
            text=f"Waiting for a connection on {host}:{port}...")

        client_socket, client_address = server_socket.accept()
        status_label.config(text=f"Connected to: {client_address}")

        with open(filename, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)

        status_label.config(text="File sent successfully.")
        server_socket.close()

    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")


# Create the main application window
root = tk.Tk()
root.title("File Transfer GUI")

# Create and place GUI widgets
button_send = tk.Button(root, text="Send File", command=send_file)
status_label = tk.Label(root, text="", fg="green")

button_send.pack()
status_label.pack()

# Start the GUI event loop
root.mainloop()
