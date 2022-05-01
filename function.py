# подключаем библиотека tkinter
import tkinter
from tkinter import *
# из библиотеки tkinter.filedialog импортируем модули asksaveasfile, askopenfile
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter import messagebox
# из библиотеки tkinter.messagebox импортируем модул showerror
from tkinter.messagebox import showerror
# импортируем файл global_variable как variable
import global_variable as variable

# глобальные перемены
name = tkinter.NONE
file_name = ''
f = False

# функция для создания нового файла


def New():
    """

    функция для создания нового файла

    Параметры
    ---

    Возвращаемые значении 
    ---

    """

    global name
    name = "Untitled"
    variable.text.delete('1.0', tkinter.END)


def Open(*args):
    """

    функция для открытия файла

    Параметры
    *args - содержыть данные нажатой кнопки (Open)

    Возвращаемые значении 
    ---

    """

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
    """

    функция для сохранения файла

    Параметры
    *args - содержыть данные нажатой кнопки (Save)

    Возвращаемые значении 
    ---

    """

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
    """

    функция для сохранения файла с возможноси выбора место и имени

    Параметры
    *args - содержыть данные нажатой кнопки (Save_As)

    Возвращаемые значении 
    ---

    """

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
    """

    функция для открытия информоционного окна с описанием нашей программы

    Параметры
    ---

    Возвращаемые значении 
    ---

    """

    messagebox.showinfo("About Text Editor", "Console text editor")


def on_closing():
    """

    функция для закрытия программы

    Параметры
    ---

    Возвращаемые значении 
    ---

    """

    if messagebox.askyesnocancel("Save changes to documens before closing", "If you don't save, changes will be lose"):
        if not f:
            print(f)
            Save_As()
        else:
            Save()
    else:
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            variable.kor.destroy()


def find():
    """

    функция для поиска строки в тексте

    Параметры
    ---

    Возвращаемые значении 
    ---

    """

    # удалить тег "found" из индекса 1 в END
    variable.text.tag_remove('found', '1.0', END)

    find_text = variable.edit1.get()

    if find_text:
        i = '1.0'
        while True:
            i = variable.text.search(find_text, i, nocase=1,
                                     stopindex=END)
            if not i:
                break

            lasti = '%s+%dc' % (i, len(find_text))
            variable.text.tag_add('found', i, lasti)
            i = lasti
        # отметят расположенную строку красным цветом
        variable.text.tag_config('found', foreground='red')
    variable.edit1.focus_set()


def replace():
    """

    функция для замены строки в тексте

    Параметры
    ---

    Возвращаемые значении 
    ---

    """

    # удалить тег "found" из индекса 1 в END
    variable.text.tag_remove('found', '1.0', END)

    # возврат к виджету
    find_text = variable.edit1.get()
    replace_text = variable.edit2.get()

    if (find_text and replace_text):
        idx = '1.0'
        while True:
            # выполняет поиск нужной строки из индекса 1
            idx = variable.text.search(find_text, idx, nocase=1,
                                     stopindex=END)
            print(idx)
            if not idx:
                break

            lastidx = '% s+% dc' % (idx, len(find_text))

            variable.text.delete(idx, lastidx)
            variable.text.insert(idx, replace_text)

            lasti = '% s+% dc' % (idx, len(replace_text))

            variable.text.tag_add('found', idx, lastidx)
            idx = lastidx

        # отметят расположенную строку зелёным цветом
        variable.text.tag_config(
            'found', foreground='green', background='yellow')
    variable.edit1.focus_set()
