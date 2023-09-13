# IndiaGovLink: Government Inventory & File Transfer Portal
## Interlab communication and Inventory Management System with port forwarding technique and tkinter GUI 
### By Adit Kaushal and Manul Rastogi

This is a brainstormed approach that was utilized after discussion. We decided to test socket programming between two different systems under the same local host network. Since basic socket programming facilitates the client and server communication on a single system on two different terminals, however under the connection of same networks two systems having the server and client code separately can also have file transfer between them.
Peer-to-peer networks are well known for file sharing between multiple computers. They establish virtual tunnels between computers to transfer data, but NATs makes it harder. A NAT, Network Address Translation, is a process which transforms private IP addresses, such as 192.168.2.1, into public addresses, such as 203.0.113.40. The idea is that multiple private addresses can hide behind a single public address and thus virtually enlarge the number of allocable public IP addresses. [Poulin-2012]

So in order to facilitate the port forwarding technique so that we can have two devices to communicate and send files between each other is by using a framework called ngrok and in turn automate using pyngrok library.Port forwarding makes the local ip to public ip. Using pyngrok we can do this by creating secure introspectable tunnels to localhost.
We are aiming to create executable files for this.

## Port forwarding using pyngrok library 
pyngrok is a Python wrapper for ngrok that manages its own binary, making ngrok available via a convenient Python API.
ngrok is a reverse proxy tool that opens secure tunnels from public URLs to localhost, perfect for exposing local web servers, building webhook integrations, enabling SSH access, testing chatbots, demoing from your own machine, and more, and its made even more powerful with native Python integration through pyngrok.

### Working of ngrok in manual form:
1. Download ngrok software from the official website
2. Now since the port and host on the sender side is 127.0.0.1 and 4900 now we can port forward it on ngrok using command ngrok tcp 4900
3. This produces a forwarded port and port url eg. 0.tcp.ngrok.io
4. Ping the port url to get the hostname in ipv4 format
5. Using this forwarded port and hostname, we can get the reciever side part

Using the pyngrok library we are able to automate the manual task of ngrok connection and hence reduce the workload of non technical people. We create tunnels to connect the sender and reciever system and securely send the files and data across the systems.
Port forwarding technique enables data transfer from server to client tricking the server to believe that the client exists on the same machine.

## Prerequisites for the program files
Before you begin, ensure you have the following installed:
- Python 3.10 or later
- tkinter
- customtkinter
- requests
- sqlite3==3.36.0
- socket
- threading
- pytz
- Pillow==9.5.0
- geoip2
- subprocess
- pyngrok==6.0.0
- xlrd==2.0.1
- pandas==1.4.2
- tabulate==0.9.0
- auto-py-to-exe==2.38.0
- pyinstaller==5.13.1

### Syntax to install: 
pip install <library-name> (windows-10 and above)
sudo apt-get install python3-pip <library-name>
             

### Setup
1. Clone the repository
2. Install the libraries tkinter, customtkinter,requests,sqlite3,Pillow==9.5.0,socket, threading,pytz,pyngrok and geoip2
3. Run the program using `py Main.py`

## 1.FILE TRANSFER GUI
### Sender Steps
To send a file, follow these steps:
1. Click on the "Sender" button.
2. Enter the file name you want to send.
3. Click on the "Send File" button.

### Receiver Steps
To receive a file, follow these steps:
1. Click on the "Receiver" button.
2. Enter the desired filename for the saving it.
3. Click on the "Receive File" button.

### Additonal information
1. User Addition is present as well
2. If you are the sender, use Sender Client only during chatting
3. If you are reciever, use Reciever Client only during chatting
4. Chatting and file transfer must not be done simultaneously
### Library Information
#### requests:
Requests is an elegant and simple HTTP library for Python, built for human beings. Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic.
#### geoip2:
The GeoIP2 object is a wrapper for the MaxMind geoip2 Python library. In order to perform IP-based geolocation, the GeoIP2 object requires the geoip2 Python package and the GeoIP Country and/or City datasets in binary format.
tkinter:
#### Tkinter
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.
#### customtkinter:
CustomTkinter is a python desktop UI-library based on Tkinter, which provides modern looking and fully customizable widgets.
#### sqlite3
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle.


### File Transfer GUI Images
Using the concepts of socket programming and geolocation coupled with threading and post requests we have created the following GUIs for file transfer that are connected and redirected on every correct step.
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/f6ff2145-e925-40b4-9477-30cc2377897f)

![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/005cad1e-bdf1-4468-b673-4e48901dd7c7)


![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/32b223ff-8583-4f8d-b638-337b40be1233)
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/a0bc5930-fb04-44a2-b882-5348286620cd)

![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/40994df9-954c-4baa-a6bb-4a90feeb7e80)

![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/e5758f07-255f-463f-9bc8-83357d5c928f)

![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/2d36c039-c422-4110-87c6-12a9c9eab3c0)
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/edf07426-f939-43dc-9558-b1b329422f72)


## 2.REAL TIME CHAT WINDOW
We have implemented a real time chat window using the similiar concepts of network programming ie socket programming and threading.
Both the sender and reciever clients have been automated using pyngrok library so that instead of manual port and host entry, the program automatically reads the port and host and forwards it to the reciever side as well.
###### Chatting and file transfer must not be done simultaneously

### Library Information:
#### AF_INET, SOCK_STREAM
AF_INET is an address family that is used to designate the type of addresses that your socket can communicate with (in this case, Internet Protocol v4 addresses). When you create a socket, you have to specify its address family, and then you can only use addresses of that type with the socket. The Linux kernel, for example, supports 29 other address families such as UNIX (AF_UNIX) sockets and IPX (AF_IPX), and also communications with IRDA and Bluetooth (AF_IRDA and AF_BLUETOOTH, but it is doubtful you'll use these at such a low level).
For the most part, sticking with AF_INET for socket programming over a network is the safest option. There is also AF_INET6 for Internet Protocol v6 addresses.

TCP (SOCK_STREAM) is a connection-based protocol. The connection is established and the two parties have a conversation until the connection is terminated by one of the parties or by a network error.

#### threading
This module constructs higher-level threading interfaces on top of the lower level _thread module.

### Method
The execution process is : 
1. run the server.py program only for the main side. Both clients should not run the server.
2. Choose the chat options from the integrated UI.
3. You will be asked to enter your name as the first entry on opening the chat window.

 ### Chat Window GUI Images
 #### server program execution
 ![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/5e00ccf2-93ad-4058-808c-eb6503d2472b)
 #### client window
 ![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/0a0b7c5a-ff6c-4926-960f-651b9b4970b9)


## 3.INVENTORY SYSTEM
### Steps
1. Download sqlite3 from the net
2. run the create_db.py and create_user_db.py programs first to create the database
3. Then you can continue with inventory applications
   
### Library Information:
#### sqlite3
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world.

#### pillow
Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. It is available for Windows, Mac OS X and Linux.

#### pytz
Pytz brings the Olson tz database into Python and thus supports almost all time zones. This module serves the date-time conversion functionalities and helps user serving international client’s base. It enables time-zone calculations in our Python applications and also allows us to create timezone aware datetime instances. 

#### os
The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system.

#### tkinter is still the backbone of the entire gui created.

### Inventory Images

### Main Page
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/88f1c7b8-3310-46fa-b4a9-8ca2424f0041)

### Employee Interface
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/d0e51229-d79d-4427-8465-78f0f200fe9f)

### Supplier Interface
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/30742a83-476e-499c-a8c8-0a92517adb3c)

### Category Interface
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/75d05ebf-177b-40e2-8d1f-1f14253cc50e)

### Product Interface
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/fc75fa69-2dee-4c76-874a-bdcce30d5964)


### Records Interface
![image](https://github.com/adit26data/Interlab-Communication-with-Inventory-Management-System/assets/98691664/f652ead4-54ee-4894-b4c5-33ea9c9ac861)

## Exe file formation
### auto-py-to-exe
A .py to .exe converter using a simple graphical interface and PyInstaller in Python.Auto PY to EXE is an amazing application for making .exe files out of your project whether it is one .py file or any number of them.

This is step is crucial as in the forked repository you will see an exe file by the name of IndiaGovLink.exe
Using auto-py-to-exe we have converted to python exe
To convert to exe:
 choose the path of mainprogram.py
 choose one file
 add all the additional files and folders except the mainprogram.py
 run the convert to .py to .exe option
 open the exe file


## Links
1.For SQLite3 download:
     https://sqlitebrowser.org/dl/
     
2.For pyngrok documentation:
      https://pyngrok.readthedocs.io/
   
3.For more research please refer these links:

FOR JAVA GUI: https://www.ijert.org/simple-file-transfer-system-using-gui-and-socket-programming-for-window-operating-system?amp=1

FOR NAT TRAVERSAL: https://www.sce.carleton.ca/~fgagnon/Publications/NATTraversal_TR_SCE-12-04.pdf
   

## License
This project is licensed under the MIT License.









