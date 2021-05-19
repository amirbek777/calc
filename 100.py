from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title("Root")
root.geometry("400x200")
root.resizable(False, False)

lab = Label(root,
	text='Часы',
	font = ('comfortaa', 30, 'bold'))
lab.pack()

lab = Label(root,
    text='--------------------------------------',
    fg = 'red',
    font = ('comfortaa', 30)) 
lab.pack()

time1 = ''
clock = Label(root,
    fg = 'green',
	font=('times', 18, 'bold'))
     
clock.pack(
	fill=BOTH,
	expand=1)

def tick():
    global time1
    time2 = time.strftime('дата и время: %m/%d/%Y, %H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(
        	text=time2)
    clock.after(200, tick)

tick()

lab = Label(root,
    text='--------------------------------------',
    fg = 'red',
    font = ('comfortaa', 30)) 
lab.pack()


root.mainloop()