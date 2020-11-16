import tkinter as tk
from tkinter import ttk 
from tkinter.scrolledtext import ScrolledText
from tkcalendar import Calendar, DateEntry
from time import strftime
todos = {}
def AddTodos(win, key, jam, menit, judul, keterangan):
    jam, menit, judul, keterangan  = [jam.get(), menit.get(), judul.get(), keterangan.get('1.0',tk.END)]
    newTodo = {
        'jam': '{}:{}'.format(jam,menit),
        'judul': judul,
        'keterangan': keterangan
        }
    if key in todos:
        todos[key].append(newTodo)
    else:
        todos[key] = [newTodo]
    ListTodo()
    win.destroy()
def ListTodo(cb=None):
    tgl = str(cal.selection_get())
    for i in treev.get_children():
        treev.delete(i)
    if tgl in todos:
        for idx,i in enumerate(todos[tgl]):
            treev.insert("", 'end', text=idx, values=(i['jam'], i['judul']))
def AddForm():
    win = tk.Toplevel()
    win.wm_title("+")
    jam = tk.IntVar(value=10)
    menit = tk.IntVar(value=30)
    judul = tk.StringVar(value='')
    tk.Label(win, text="Waktu:").grid(row=0,column=0)
    tk.Spinbox(win,from_=0,to=23,textvariable=jam,width=3).grid(row=0, column=1)
    tk.Spinbox(win,from_=0,to=59,textvariable=menit,width=3).grid(row=0, column=2)
    tk.Label(win, text="Judul:",).grid(row=1,column=0)
    tk.Entry(win,textvariable=judul).grid(row=1, column=1, columnspan=2)
    tk.Label(win, text="Keterangan:").grid(row=2,column=0)
    keterangan = ScrolledText(win, width=12, height=5)
    keterangan.grid(row=2, column=1, columnspan=2, rowspan=4)
    ttk.Button(win, text="Tambah", command=lambda: AddTodos(win, str(cal.selection_get()),jam,menit,judul,keterangan)).grid(row=10, column=0)
def DelTodo():
    curItem = treev.focus()
    todos[str(cal.selection_get())].pop(treev.item(curItem)['text'])
    ListTodo()
def LoadTodos():
    global todos
    f = open('mytodo.dat','r')
    data=f.read()
    f.close()
    todos = eval(data)
    ListTodo()
def SaveTodos():
    f = open('mytodo.dat','w')
    f.write(str(todos))
    f.close()
def Title(): 
    string = strftime('%H:%M') 
    root.title(str(cal.selection_get()) + " | " + string + " | Calendar Todo")
    root.after(1000, Title)

root = tk.Tk()
s = ttk.Style()
s.configure('Treeview', rowheight=16) 
root.title("Calendar Todo")
cal = Calendar(root, font="Arial 14", selectmode='day', locale='id_ID',
                cursor="hand1")
cal.bind( "<<CalendarSelected>>", ListTodo )
cal.grid(row=0, column=0, sticky='W',rowspan=8)
treev = ttk.Treeview(root) 
treev.grid(row=0, column=1, sticky='WNE', rowspan=3, columnspan=2)

scorllBar = tk.Scrollbar(root)
scorllBar.grid(row=0, column=2, sticky='ENS', rowspan=4)
treev.configure(xscrollcommand = scorllBar.set) 
scorllBar.config(command=treev.yview)
treev["columns"] = ("1", "2") 

treev['show'] = 'headings'

treev.column("1", width = 50) 
treev.column("2", width = 150) 

treev.heading("1", text ="JAM") 
treev.heading("2", text ="JUDUL")
buttonAdd = tk.Button(root, text="Add task",width=20, command=AddForm)
buttonAdd.grid(row=5, column=1, sticky='W')

buttonDelete = tk.Button(root, text="Delete task",width=20, command=DelTodo)
buttonDelete.grid(row=5, column=2, sticky='W')

buttonLoad = tk.Button(root, text="Load tasks",width=20, command=LoadTodos)
buttonLoad.grid(row=6, column=1, sticky='W')

buttonSave = tk.Button(root, text="Save tasks",width=20, command=SaveTodos)
buttonSave.grid(row=6, column=2, sticky='W')
Title()
root.mainloop()