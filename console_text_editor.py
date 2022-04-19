from cProfile import label
from tkinter import*
import tkinter
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from click import command

name = tkinter.NONE
file_name = ''
f = False

def New():
    global name
    name = "Untitled"
    text.delete('1.0', tkinter.END)

def Open(*args):
    global name
    global f
    p = askopenfile(mode="r")
    if p is None:
        return
    name = p.name
    t = p.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', t)
    f = True

def Save(*args):
    global f
    if (f == False):
        Save_As()
    else:
        s = text.get('1.0', tkinter.END)
        t = open(file_name, 'w')
        t.write(s)
        t.close()
    f = True


def Save_As(*args):
    global file_name
    t = asksaveasfile(mode='w', defaultextension='.txt')
    s = text.get('1.0', tkinter.END)
    try:
        t.write(s.rstrip())
    except Exception:
        showerror(title="Error", message="Saving file error")
    else:
        file_name = t.name

def on_closing():
    if messagebox.askyesnocancel("Save changes to documens before closing", "If you don't save, changes will be lose"):
        if not f:
            print(f)
            Save_As()
        else:
            Save()
    else:
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            kor.destroy()

def Info():
    messagebox.showinfo("About Text Editor", "Console text editor")

kor = Tk()
text = Text(kor, width=500, height=500, wrap="word")
sc = Scrollbar(kor, orient=VERTICAL, command=text.yview)
kor.title("Text Editor") 
kor.geometry('600x550')
sc.pack(side="right", fill="y")
text.configure(yscrollcommand=sc.set)
text.pack()
menust = tkinter.Menu(kor)
m = tkinter.Menu(menust)
m.add_command(label = "New File" ,command=New)
m.add_command(label = "Open File", command=Open)
m.add_command(label = "Save", command=Save)
m.add_command(label = "Save As...", command=Save_As)
menust.add_cascade(label ="File",underline=0, menu=m)
menust.add_command(label = "Info", command=Info)
menust.add_command(label = "Exit", command=on_closing)
kor.bind('<Control-s>', Save)
kor.bind('<Control-S>', Save)
kor.bind('<Control-Shift-s>', Save_As)
kor.bind('<Control-Shift-S>', Save_As)
kor.bind('<Control-o>', Open)
kor.bind('<Control-O>', Open)
kor.config(menu=menust)
kor.protocol("WM_DELETE_WINDOW", on_closing)

kor.mainloop()