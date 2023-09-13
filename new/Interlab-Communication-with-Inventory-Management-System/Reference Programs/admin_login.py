from tkinter import *
import tkinter as tk
from tkinter import ttk
# import tkinter.messagebox as tkmb 
win = Tk()
win.geometry("550x350")
icon_path = "iconimage.ico"
win.iconbitmap(icon_path)
def entry_update(text):
   entry.delete(0,END)
   entry.insert(0,text)

entry= Entry(win, width= 30, font=("Microsoft Yahei UI Light",9,"bold"),bg= "white")
entry.pack(padx=10,pady=25)
# entry.label()
button_dict={}
option= ["Mangalore DRDO","Chennai DRDO","Manipur College Lab","INMAS DRDO"]
# option.pack(padx=10,pady=20)
for i in option:
   def func(x=i):
      return entry_update(x)
   win.title("INMAS DRDO")

   button_dict[i]=ttk.Button(win,width=40,text=i,command= func)
   button_dict[i].pack()
heading=Label(win,text="Select The Lab To Communicate",font=("Microsoft Yahei UI Light",9,"bold"),bg='white')
heading.place(x=175,y=46)   
# tkmb.showinfo(message="Select The Lab to communicate:")
win.mainloop()
