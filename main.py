import tkinter as tk
from tkcalendar import Calendar, DateEntry
from time import strftime 
def listTodo(cb):
    print(cal.selection_get())
def add_task():
    pass
def del_task():
    pass
def load_task():
    pass
def save_task():
    pass
def title(): 
    string = strftime('%H:%M:%S %p') 
    root.title(str(cal.selection_get()) + " | " + string + " | Calendar Todo")
    root.after(1000, time) 

root = tk.Tk()
root.title("Calendar Todo")
cal = Calendar(root, font="Arial 14", selectmode='day', locale='id_ID',
                cursor="hand1")
cal.bind( "<<CalendarSelected>>", listTodo )
cal.grid(row=0, column=0, sticky='W',rowspan=8)
listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.grid(row=0, column=1, sticky='NS', rowspan=4, columnspan=2)

scrollbar_tasks = tk.Scrollbar(root)
scrollbar_tasks.grid(row=0, column=2, sticky='ENS', rowspan=4)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

button_add_task = tk.Button(root, text="Add task",width=20, command=add_task)
button_add_task.grid(row=5, column=1, sticky='W')

button_delete_task = tk.Button(root, text="Delete task",width=20, command=del_task)
button_delete_task.grid(row=5, column=2, sticky='W')

button_load_tasks = tk.Button(root, text="Load tasks",width=20, command=load_task)
button_load_tasks.grid(row=6, column=1, sticky='W')

button_save_tasks = tk.Button(root, text="Save tasks",width=20, command=save_task)
button_save_tasks.grid(row=6, column=2, sticky='W')
title()
root.mainloop()