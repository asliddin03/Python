
import tkinter
import global_variable as variable
from tkinter import *
from click import command 
from function import New, Open, Save, Save_As, Info, on_closing, find, replace 
sc = Scrollbar(variable.kor, orient=VERTICAL, command=variable.text.yview)
sc.pack(side="right", fill="y")
variable.text.configure(yscrollcommand=sc.set)

variable.text.pack()

# Заголовок экрана
variable.kor.title("Text Editor")

# размер экрана
variable.kor.geometry('600x550')

menust = tkinter.Menu(variable.kor)
m = tkinter.Menu(menust)

# нашим кнопкам привяжем действия, при нажатии каждую из них направляем на соответствующую функцию
m.add_command(label="New File", command=New)
m.add_command(label="Open File", command=Open)
m.add_command(label="Save", command=Save)
m.add_command(label="Save As...", command=Save_As)

menust.add_cascade(label="File", underline=0, menu=m)

menust.add_command(label="Info", command=Info)
menust.add_command(label="Exit", command=on_closing)

variable.kor.config(menu=menust)

# с помощью клавиши исполняем соответствующие команды
variable.kor.bind('<Control-s>', Save)
variable.kor.bind('<Control-S>', Save)
variable.kor.bind('<Control-Shift-s>', Save_As)
variable.kor.bind('<Control-Shift-S>', Save_As)
variable.kor.bind('<Control-o>', Open)
variable.kor.bind('<Control-O>', Open)

variable.kor.protocol("WM_DELETE_WINDOW", on_closing)

variable._find.config(command=find)
variable.repl.config(command=replace)

# функция # mainloop вызывает бесконечный цикл окна, так что окно будет
# дождитесь любого взаимодействия с пользователем, пока мы закрой его
variable.kor.mainloop()
