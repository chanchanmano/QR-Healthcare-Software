import tkinter as tk
from tkinter import ttk
from tkinter import *
from sqlpack import sql
import guifunc
from tkinter import messagebox


def info():
	messagebox.showinfo("Information","This window requires you to enter \n the access code of your Organisation\n to access the database")

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = accesscodebox.get()
	return userInput


# this is the function called when the button is clicked
def checkaccess():
	a = getInputBoxValue()
	checker = sql.Mcheck_value(a)
	if checker:
		root.destroy()
		guifunc.scanqrgui()


root = Tk()

# This is the section of code which creates the main window
root.geometry('360x230')
root.configure(background='#F0F8FF')
root.title('Apollo Systems')
p1 = PhotoImage(file='C:/Users/Aryan-PC/PycharmProjects/testproject/icon.png')
root.iconphoto(False, p1)

menubar = Menu(root)
menubar.add_command(label="Info", command=info)
menubar.add_command(label="Quit", command=root.quit)

# This is the section of code which creates a text input box
accesscodebox=Entry(root)
accesscodebox.place(x=113, y=97)


# This is the section of code which creates the a label
Label(root, text='Enter Organisation\'s Access Code ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=63, y=57)


# This is the section of code which creates a button
Button(root, text='Access Database', bg='#DEDEDE', font=('arial', 12, 'normal'), command=checkaccess).place(x=103, y=137)

root.config(menu=menubar)
root.mainloop()
