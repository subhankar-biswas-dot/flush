########## SOURCE CODE OF FIRST APP---A SIMPLE CALCULATOR ###########
from tkinter import *
import tkinter as tk
from tkinter import messagebox as tkMessageBox

def process():
    number1=Entry.get(e1)
    number2=Entry.get(e2)
    operator=Entry.get(e3)

    number1=int(number1)
    number2=int(number2)
    if operator == "+":
        answer=number1+number2
    if operator == "-":
        answer=number1-number2
    if operator == "*":
        answer=number1*number2
    if operator == "/":
        answer=number1/number2
    Entry.insert(e4,0,answer)
    print(answer)

top=tk.Tk()
l1=Label(top,text="My Claculator",).grid(row=0,column=1)
l2=Label(top,text="First Number",).grid(row=1,column=0)
l1=Label(top,text="Second Number",).grid(row=2,column=0)
l1=Label(top,text="Operator",).grid(row=3,column=0)
l1=Label(top,text="Answer",).grid(row=4,column=0)

e1=Entry(top,bd=5)
e1.grid(row=1,column=1)
e2=Entry(top,bd=5)
e2.grid(row=2,column=1)
e3=Entry(top,bd=5)
e3.grid(row=3,column=1)
e4=Entry(top,bd=5)
e4.grid(row=4,column=1)
B=Button(top,text="Submit",command=process).grid(row=5,column=1,)

top.mainloop()
