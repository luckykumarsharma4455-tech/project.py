import tkinter as tk 
from tkinter import,messagebox

#funtion
def add_task():
    task=entry.get()
    if task !="":
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
        else:
         massagebox.showwarning("warning","task cannot be empty!")    


    def remove_task():
        try:
            selected=listbox.curselection()[0]
            listbox.delete(selected)

     except indexError:
         massagebox.showwarning("Warning","Please select a task to remove!")

    def update_task():
        try:
            selected=listbox.curselection()[0]
            new_task=entry.get()
    if new_task!="":
        listbox.delete(selected)
        listbox.insert(selected,new_task)
        entry.delete(0,tk.END)
    else:
     messagebox.showwarning("Warning","updated task cannot be empty!")

    except indexError:

    massagebox.showwarning("Warning","please select a taskto update!")
     def exit_app():

     root.destroy()

     #GUI setup

    root=tk.Tk()

    root.title("To-Do List App")

    root.geometry("400x400")

    root.config(bg-■"#f5f5f5")

    #Input field

    entry = tk.Entry(root,width=30,font=("Arial",14))
    entry.pack(pady=10)


    #Buttons

    btn_frame=tk.Frame(root,bg="#f5f5f5")
     btn_frame.pack(pady=5)


    tk.Button(btn_frame,text="Add task",width=10,command=add_task).grid(row=0,
        column=0,padx=5)

    tk.Button(btn_frame,text="Remove Task",width=12,command=remove_task).grid(row=0,column=1,padx=5)

    tk.Button(btn_frame,task="Update Task",width=12,command=update_task).grid(row=0,column=2,padx=5)
    tk.Button(root,text="Exit",width=10, command=exit_app).pack(pady=5)

    #Task list
    listbox = tk.listbox(root,width=40,height=10,font=("Arial",12))
    listbox.pack(pady=10)

    root.mainloop
