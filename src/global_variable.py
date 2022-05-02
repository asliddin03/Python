import tkinter as tk


kor = tk.Tk()
text = tk.Text(kor, width=500, height=500, wrap="word")
fram = tk.Frame(kor)

edit1 = tk.Entry(fram)
edit1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
edit1.focus_set()

_find = tk.Button(fram, text='Find')
_find.pack(side=tk.LEFT)

edit2 = tk.Entry(fram)
edit2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
edit2.focus_set()

repl = tk.Button(fram, text='Replace')
repl.pack(side=tk.LEFT)

fram.pack(side=tk.TOP)
