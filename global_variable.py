import tkinter
from tkinter import *


kor = tkinter.Tk()
text = Text(kor, width=500, height=500, wrap="word")
fram = Frame(kor)

edit1 = Entry(fram)
edit1.pack(side=LEFT, fill=BOTH, expand=1)
edit1.focus_set()

_find = Button(fram, text='Find')
_find.pack(side=LEFT)

edit2 = Entry(fram)
edit2.pack(side=LEFT, fill=BOTH, expand=1)
edit2.focus_set()

repl = Button(fram, text='Replace')
repl.pack(side=LEFT)

fram.pack(side=TOP)
