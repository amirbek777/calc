from tkinter import *
from tkinter import messagebox

def btn_click():
    x = ent.get()
    try:
       lab ['text'] = str(eval(x))
    except: messagebox.showerror('ошибка, не правильно введенные данные')



root = Tk()
root.title("AmirbekRoot")
root.geometry("250x200")
root.resizable(False, False)

menu = Label(root, text= 'Калькулятор', font = ('Arial Bond', 10, 'bold'))
menu.pack()
ent = Entry(root, text='', font = ('Arial Bond', 25,'bold'), width = 9)
ent.pack()
Button(root, text='Решить пример', font = ('Arial bond', 17, 'bold'), command = btn_click).pack()
lab = Label(root, text='0', font = ('Arial Bond', 19, 'bold'))
lab.pack()

root.mainloop()
