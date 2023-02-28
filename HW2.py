from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image

GUI=Tk()
GUI.title('โปรแกรมสั่งสินค้า')
GUI.geometry('500x500')

img1 = Image.open("B101 keyboard.jpeg")
img2 = Image.open("B102 mouse.jpeg")

img1 = img1.resize((50, 30))
img2 = img2.resize((50, 30))

tk_img1 = ImageTk.PhotoImage(img1)
tk_img2 = ImageTk.PhotoImage(img2)


def update_number_box1(*arg):
    number_box1.delete(0,tk.END)
    number_box1.insert(0,n1.get())

def update_number_box2(*arg):
    number_box2.delete(0,tk.END)
    number_box2.insert(0,n2.get())


L_head=Label(GUI,text='รายการสั่งสินค้า',font=('Cordia New',30),fg='red')
L_head.pack()
L_item1=Label(GUI,text='B-101 keyboard',font=('Cordia New',20),fg='black')
L_item1.place(x=90,y=100)
L_item2=Label(GUI,text='B-102 mouse',font=('Cordia New',20),fg='black')
L_item2.place(x=90,y=150)

image_label1 = Label(GUI, image=tk_img1)
image_label1.place(x=30,y=100)
image_label2 = Label(GUI, image=tk_img2)
image_label2.place(x=30,y=150)


n1=IntVar()
n2=IntVar()
total_item=IntVar()
n1.set(0)
n2.set(0)
total_item.set(0)

def Itemno1plus():
    n1.set(n1.get()+1)
    
def Itemno1minus():
    n1.set(n1.get()-1)

def Itemno2plus():
    n2.set(n2.get()+1)

def Itemno2minus():
    n2.set(n2.get()-1)
    messagebox.showinfo('ยอดการสั่งซื้อ')

def Total():
    total_item.set(n1.get()+n2.get())
    text = 'รวมยอดการสั่งซื้อทั้งหมด ' + str(total_item.get()) +' ชิ้น'
    messagebox.showinfo(' ',text)
    

    
Bp_item_no1=Button(GUI,text='+',command=Itemno1plus)
Bp_item_no1.place(x=370,y=100)
Bm_item_no1=Button(GUI,text='-',command=Itemno1minus)
Bm_item_no1.place(x=410,y=100)

Bp_item_no2=Button(GUI,text='+',command=Itemno2plus)
Bp_item_no2.place(x=370,y=150)
Bm_item_no2=Button(GUI,text='-',command=Itemno2minus)
Bm_item_no2.place(x=410,y=150)

    
FB1=Frame(GUI)
FB1.place(x=400,y=400)
Check=Button(GUI,text='สรุปยอด',command=Total)
Check.place(x=400,y=400)

number_box1=Entry(GUI,width=5)
number_box1.insert(0,n1.get())
number_box1.place(x=300,y=100)

number_box2=Entry(GUI,width=5)
number_box2.insert(0,n2.get())
number_box2.place(x=300,y=150)



n1.trace("w", update_number_box1)
n2.trace("w", update_number_box2)

GUI.mainloop()
