from tkinter import *
import tkinter as tk
from tkinter import messagebox as tkMessageBox
def clicked():
    text=Entry.get(txt1)
    text="WELLCOME "+ str(text)
    Entry.insert(txt2,0,text)
    tkMessageBox.showinfo('Message Title','Compiled Successfully')
    print(text)
window=tk.Tk()

label=Label(window,text="FIRST APP",font=("Arial Bold",50)).grid(row=0,column=0)
label1=Label(window,text="ENTER YOUR NAME",).grid(row=1,column=0)
label3=Label(window,text="OUTPUT").grid(row=3,column=0)
txt1=Entry(window,bd=5)
txt1.grid(row=1,column=1)
txt2=Entry(window,bd=5)
txt2.grid(row=3,column=1)
bt=tk.Button(window,text="ENTER",command=clicked,bg="orange",fg="red",).grid(row=4,column=0)
window.mainloop()
