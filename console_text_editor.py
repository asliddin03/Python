import tkinter
from tkinter import *
from click import command
import global_variable as variable
from function import New, Open, Save, Save_As, Info, on_closing

sc = Scrollbar(variable.kor, orient=VERTICAL, command=variable.text.yview)
sc.pack(side="right", fill="y")
variable.text.configure(yscrollcommand=sc.set)

variable.text.pack()

variable.kor.title("Text Editor") 

variable.kor.geometry('600x550')

menust = tkinter.Menu(variable.kor)
m = tkinter.Menu(menust)

m.add_command(label = "New File" ,command=New)
m.add_command(label = "Open File", command=Open)
m.add_command(label = "Save", command=Save)
m.add_command(label = "Save As...", command=Save_As)

menust.add_cascade(label ="File",underline=0, menu=m)

menust.add_command(label = "Info", command=Info)
menust.add_command(label = "Exit", command=on_closing)

variable.kor.config(menu=menust)

variable.kor.bind('<Control-s>', Save)
variable.kor.bind('<Control-S>', Save)
variable.kor.bind('<Control-Shift-s>', Save_As)
variable.kor.bind('<Control-Shift-S>', Save_As)
variable.kor.bind('<Control-o>', Open)
variable.kor.bind('<Control-O>', Open)

variable.kor.protocol("WM_DELETE_WINDOW", on_closing)

variable.kor.mainloop()