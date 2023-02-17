from tkinter import *
from tkinter import ttk
from random import *
# объект
root = Tk()
# геометрия
root.geometry("500x500")
root.title("КМН")
# хранилище
list = ["Камень","Бумага","Ножницы"]
choose_number = randint(0,2)
label = Label(root,text="Ваш выбор",width = 20,height=4,font=("calibri",15))
label.pack()
def spin():
    choose_number = randint(0,2)
    label.config(text=list[choose_number])
    if user_select.get() == "Камень":
        user_select_value = 0
        print(user_select_value)
    elif user_select.get() == "Бумага":
        user_select_value = 1
        print(user_select_value)
    elif user_select.get() == "Ножницы":
        user_select_value = 2
        print(user_select_value)
    if user_select_value == 0:
        if choose_number == 0:
            wl_label.config(text="Ничья")
        elif choose_number == 1:
            wl_label.config(text="Вы проиграли:(")
        elif choose_number == 2 :
            wl_label.config(text="Вы виграли!!!!")
    elif user_select_value == 1:
        if choose_number == 1:
            wl_label.config(text="Ничья")
        elif choose_number == 0:
            wl_label.config(text="Вы виграли!!!!")
        elif choose_number == 2 :
            wl_label.config(text="Вы проиграли:(")
    elif user_select_value == 2:
        if choose_number == 2:
            wl_label.config(text="Ничья")
        elif choose_number == 0:
            wl_label.config(text="Вы проиграли:(")
        elif choose_number == 1 :
            wl_label.config(text="Вы виграли!!!!")
# Добавление выпадающего списка для камня, бумаги, ножниц
user_select = ttk.Combobox(root,value=["Камень","Бумага","Ножницы"])
user_select.current(0)
user_select.pack()
# добавление кнопки
wl_label = Label(root,text="",font=("arial",10),width=50,height=4)
wl_label.pack()
button = Button(root,text="начать",font=("bell mt",10),command=spin)
button.pack()
root.mainloop()