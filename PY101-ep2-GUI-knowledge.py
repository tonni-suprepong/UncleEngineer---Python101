from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('Know your POOP')
GUI.geometry('620x600')

L1 = Label(GUI,text="Your POOP color",font=("Arial Bold", 50))
L1.place(x=30,y=40)

FB1 = Frame(GUI)
FB1.place(x=20,y=150)

FB2 = Frame(GUI)
FB2.place(x=220,y=150)

FB3 = Frame(GUI)
FB3.place(x=420,y=150)

FB4 = Frame(GUI)
FB4.place(x=20,y=350)

FB5 = Frame(GUI)
FB5.place(x=220,y=350)

FB6 = Frame(GUI)
FB6.place(x=420,y=350)


def Poop1():
    text = 'yellow poop - Fat is stool, malabsorption issures'
    messagebox.showinfo('symptoms',text)

def Poop2():
    text = 'brown poop - Normal'
    messagebox.showinfo('symptoms',text)

def Poop3():
    text = 'dark-brown poop - Normal'
    messagebox.showinfo('symptoms',text)

def Poop4():
    text = 'green poop - Excess bile, change in diet, diarrhea'
    messagebox.showinfo('symptoms',text)

def Poop5():
    text = 'black poop - Bleeding in upper GI tract'
    messagebox.showinfo('symptoms',text)

def Poop6():
    text = 'red poop - Bleeding in lower GI tract'
    messagebox.showinfo('symptoms',text)




imgPoop1 = PhotoImage(file='PY101-ep2 - yellow.png')
B1 = ttk.Button(FB1,image=imgPoop1,command=Poop1)
B1.pack(ipadx=10,ipady=10)


imgPoop2 = PhotoImage(file='PY101-ep2 - brown.png')
B2 = ttk.Button(FB2,image=imgPoop2,command=Poop2)
B2.pack(ipadx=10,ipady=10)

imgPoop3 = PhotoImage(file='PY101-ep2 - dark-brown.png')
B3 = ttk.Button(FB3,image=imgPoop3,command=Poop3)
B3.pack(ipadx=10,ipady=10)

imgPoop4 = PhotoImage(file='PY101-ep2 - grey.png')
B4 = ttk.Button(FB4,image=imgPoop4,command=Poop4)
B4.pack(ipadx=10,ipady=10)


imgPoop5 = PhotoImage(file='PY101-ep2 - black.png')
B5 = ttk.Button(FB5,image=imgPoop5,command=Poop5)
B5.pack(ipadx=10,ipady=10)

imgPoop6 = PhotoImage(file='PY101-ep2 - red.png')
B6 = ttk.Button(FB6,image=imgPoop6,command=Poop6)
B6.pack(ipadx=10,ipady=10)


GUI.mainloop()
