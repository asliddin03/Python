import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
import global_variable as variable


name = tkinter.NONE
file_name = ''
f = False

def New():
    global name
    name = "Untitled"
    variable.text.delete('1.0', tkinter.END)

def Open(*args):
    global name
    global f
    p = askopenfile(mode="r")
    if p is None:
        return
    name = p.name
    t = p.read()
    variable.text.delete('1.0', tkinter.END)
    variable.text.insert('1.0', t)
    f = True

def Save(*args):
    global f
    if (f == False):
        Save_As()
    else:
        s = variable.text.get('1.0', tkinter.END)
        t = open(file_name, 'w')
        t.write(s)
        t.close()
    f = True


def Save_As(*args):
    global file_name
    t = asksaveasfile(mode='w', defaultextension='.txt')
    s = variable.text.get('1.0', tkinter.END)
    try:
        t.write(s.rstrip())
    except Exception:
        showerror(title="Error", message="Saving file error")
    else:
        file_name = t.name

def Info():
    messagebox.showinfo("About Text Editor", "Console text editor")

def on_closing():
    if messagebox.askyesnocancel("Save changes to documens before closing", "If you don't save, changes will be lose"):
        if not f:
            print(f)
            Save_As()
        else:
            Save()
    else:
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            variable.kor.destroy()
