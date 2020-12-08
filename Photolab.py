from tkinter import *
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as fd
from PIL import Image,ImageTk
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
#creating root that Extends Tk
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("PHOTO LAB")
        self.geometry('{}x{}'.format(940,600))
       # self.c=tk.Canvas(self,width=940,height=600)
        img=ImageTk.PhotoImage(Image.open('/home/subhankar/background.jpeg').resize((940,600),Image.ANTIALIAS))
       # self.c.create_image(0,0,anchor=NW,image=img)
        self.label=PhotoImage(file="/home/subhankar/background.jpeg")
        self.label=Label(self,image=img)
       # self.wm_iconbitmap('icon.ico')
        self.labelFrame=tk.LabelFrame(self,text="open File")
        self.labelFrame.grid(column=0,row=1)
        self.button()
    def button(self):
        self.button=tk.Button(self.labelFrame,text="Browse A File",command=self.fileDial)
        self.button.grid(column=1,row=1)
    def fileDial(self):
        self.filename=fd.askopenfilename(initialdir="/",title="Select A File",filetypes=(("jpeg files","*.jpeg"),("png files","*.png"),("all files","*.*")))
        self.op=tk.Entry(self.labelFrame,bd=5)
        self.op.grid(column=1,row=2)
        tk.Entry.insert(self.op,0,self.filename)
        text=tk.Entry.get(self.op)
        self.showImg(text)
        print(text)

    def showImg(self,text):
        global img
       # img=Image.open(text)
        #img=img.resize((300,300),Image.ANTIALIAS)
        img=cv2.imread(text,cv2.IMREAD_COLOR)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img=cv2.resize(img,(600,600))
        img=self.cartoonify(text,img)
        self.im=Image.fromarray(img)
        self.img_tk=ImageTk.PhotoImage(image=self.im)
        self.panel=tk.Label(self.labelFrame,image=self.img_tk,width=600,height=600).grid(row=3,column=1)
        self.cartoonify(text,img)
    def cartoonify(self,text,img_rgb):
        numFilter=4
        img_color=img_rgb
        for _ in range(numFilter):
            img_color=cv2.bilateralFilter(img_color,15,30,20)
        img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY)
        img_blur=cv2.medianBlur(img_gray,7)
        img_edge=cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)
        img_edge=cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
        return cv2.bitwise_and(img_color,img_edge)

root=Root()
#root.configure(background='#001166')
#root.geometry('{}x{}'.format(940,600))
#c=Canvas(root,width=600,height=600)
#my_img=ImageTk.PhotoImage(Image.open('/home/subhankar/background.jpeg'))
#c.background=my_img
#c.create_image(0,0,anchor=NW,image=my_img)
root.mainloop()
