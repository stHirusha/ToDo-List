from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from datetime import datetime
from PIL import ImageTk,Image

root = Tk()
root.title("To-Do List")
root.geometry("300x500+10+10")
root.resizable(False,False)
root.iconbitmap("Image/icon.ico")

def show_date():
   date_str = strftime("%A, %B %d, %Y")
   date.config(text=date_str)
   date.after(1000,show_date)

def show_time():
   time_str = strftime("%H:%M:%S")
   time.config(text=time_str)
   time.after(1000,show_time)

def add_task():
   window = Toplevel(root)
   window.title("Add Task")
   window.geometry("300x400+330+10")
   window.resizable(False,False)

   def save_task():
      x = "@"

      task_main= str(task.get())

      if len(task_main) > 0:
         listbox.insert(END,f"{x}. {task_main}")
      else:
         messagebox.showerror("Error","Please fill the inputs")
      
   task = StringVar()

   text = Label(window,text="Add Task",font=("Times New Roman",15,"bold"))
   text.pack(padx=20,pady=5)

   text_1 = Label(window,text="What needs to be done?",font=("Times New Roman",12))
   text_1.pack(padx=20,anchor="nw")
   entry = Entry(window,font=("Times New Roman",12),bg="#b3b5b4",textvariable=task)
   entry.pack(padx=20,pady=(5,0),anchor="nw",fill="x")

   save = Button(window,text="Save",font=("Times New Roman",15,"bold"),width=10,command=save_task)
   save.pack(side="bottom",pady=10)

def delete():
   listbox.delete(ANCHOR)
   
   
date = Label(root,font=("Times New Roman",15,"bold"))
date.pack(padx=20,pady=(10,2))
show_date()

time = Label(root,font=("Times New Roman",12,"bold"))
time.pack(padx=20,pady=(0,10))
show_time()

frame_1 = LabelFrame(root,text="To Do List",font=("Times New Roman",12),width=280,height=200,padx=10,pady=10)
frame_1.pack(padx=10,pady=(0,10),fill="both",expand=True)

listbox= Listbox(frame_1,font=("Times New Roman",12),cursor='hand2')
listbox.pack(side=LEFT,fill=BOTH,expand=1,padx=2)
scrollbar = Scrollbar(frame_1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

add = Button(root,text="Add Task",font=("Times New Roman",15,"bold"),command=add_task)
add.pack(side="left",pady=10,padx=10)

delete = Button(root,text="Delete Task",font=("Times New Roman",15,"bold"),command=delete)
delete.pack(side="right",pady=10,padx=10)

frame_1.pack_propagate(False)

root.mainloop()
