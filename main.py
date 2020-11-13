import tkinter as tk
from tkcalendar import Calendar, DateEntry

def listTodo(cb):
    print(cal.selection_get())

root = tk.Tk()
root.title("Calendar Todo")
cal = Calendar(root, font="Arial 14", selectmode='day', locale='id_ID',
                cursor="hand1")
cal.bind( "<<CalendarSelected>>", listTodo )
cal.grid(row=0, column=0)
root.mainloop()