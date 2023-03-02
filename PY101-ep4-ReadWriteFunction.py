from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from datetime import datetime

import csv

# --------------------------------
# Main Parameter Section
# --------------------------------
fileName = 'log - food before poop.csv'

picPoop1 = 'PY101-ep2 - yellow.png'
picPoop2 = 'PY101-ep2 - brown.png'
picPoop3 = 'PY101-ep2 - dark-brown.png'
picPoop4 = 'PY101-ep2 - grey.png'
picPoop5 = 'PY101-ep2 - black.png'
picPoop6 = 'PY101-ep2 - red.png'

# --------------------------------
# Function Section
# --------------------------------

#work with CSV
def writingCSV(fileName,dataList):
    with open(fileName, 'a',encoding='utf-8',newline='') as file_object:
        lines = csv.writer(file_object)
        lines.writerow(dataList)

# POPUP Function
def popupInsertFood(poopColor,poopSymtom):
    tp = Toplevel(GUI)
    tp.geometry("500x200")

    textinfo = poopColor  + ' - ' + poopSymtom
    popup_info= Label(tp, text=textinfo)
    popup_info.pack(ipadx=10,ipady=10)

    popup_guid= Label(tp, text='What did you eat before poop?')
    popup_guid.pack(ipadx=10,ipady=10)

    entry1= Entry(tp, width= 20) #input text - food
    entry1.pack()
    entry1.focus_set() #set cursor to the text entry

    def controlSubmit():
        saveandexit(poopColor)
        tp.destroy()
        displayCSV()


    def saveandexit(poopColor):
        textTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_data = entry1.get()
        format_save_data = [textTime,poopColor,save_data]
        writingCSV(fileName,format_save_data)     

        messagebox.showinfo('inform','save successful')              
        

    Button(tp,text= "submit", command= controlSubmit).pack(pady= 5,side=TOP)
    


#work with CSV
def displayCSV():
    def readingCSV(CSVfile):

        #Handling the FileNotFoundError exception
        try:
            with open(CSVfile) as file_object:
                lines = file_object.readlines()
        except FileNotFoundError:
            msg = "Can't find file {0}.".format(CSVfile)
            print(msg)
            with open(CSVfile, 'w') as file_object:
                file_object.write("")



        with open(CSVfile,encoding='utf-8',newline='') as file_object:
            #lines = file_object.readlines() #export to List
            lines = csv.reader(file_object,delimiter=',')
            retuenData = list(lines ) 

        return retuenData #return in List

    displayData = readingCSV(fileName)

    endlist = mylist.size()
    mylist.delete('0', endlist )  #Object List box
    for row in displayData:
        mylist.insert(END, row[0] + ' - ' + row[1] + ' - ' + row[2] + '\n')


def Poop1():
    poopColor = 'yellow poop'
    poopSymtom = 'Fat is stool, malabsorption issures'
    popupInsertFood(poopColor,poopSymtom)

def Poop2():
    poopColor = 'brown poop'
    poopSymtom = 'Normal'
    popupInsertFood(poopColor,poopSymtom)

def Poop3():
    poopColor = 'dark-brown poop'
    poopSymtom = 'Normal'
    popupInsertFood(poopColor,poopSymtom)

def Poop4():
    poopColor = 'green poop'
    poopSymtom = 'Excess bile, change in diet, diarrhea'
    popupInsertFood(poopColor,poopSymtom)

def Poop5():
    poopColor = 'black poop'
    poopSymtom = 'Bleeding in upper GI tract'
    popupInsertFood(poopColor,poopSymtom)

def popup_Poop6():
    poopColor = 'red poop'
    poopSymtom = 'Bleeding in lower GI tract'
    popupInsertFood(poopColor,poopSymtom)


# --------------------------------
# GUI Section
# --------------------------------

GUI = Tk()
GUI.title('Know your POOP')
GUI.geometry('1200x600')

# -- LEFT Section --
L1 = Label(GUI,text="Your POOP color",font=("Arial Bold", 50))
L1.place(x=30,y=40)

FB1 = Frame(GUI)
FB1.place(x=20,y=150)
imgPoop1 = PhotoImage(file=picPoop1)
B1 = ttk.Button(FB1,image=imgPoop1,command=Poop1)
B1.pack(ipadx=10,ipady=10)

FB2 = Frame(GUI)
FB2.place(x=220,y=150)
imgPoop2 = PhotoImage(file=picPoop2)
B2 = ttk.Button(FB2,image=imgPoop2,command=Poop2)
B2.pack(ipadx=10,ipady=10)

FB3 = Frame(GUI)
FB3.place(x=420,y=150)
imgPoop3 = PhotoImage(file=picPoop3)
B3 = ttk.Button(FB3,image=imgPoop3,command=Poop3)
B3.pack(ipadx=10,ipady=10)

FB4 = Frame(GUI)
FB4.place(x=20,y=350)
imgPoop4 = PhotoImage(file=picPoop4)
B4 = ttk.Button(FB4,image=imgPoop4,command=Poop4)
B4.pack(ipadx=10,ipady=10)

FB5 = Frame(GUI)
FB5.place(x=220,y=350)
imgPoop5 = PhotoImage(file=picPoop5)
B5 = ttk.Button(FB5,image=imgPoop5,command=Poop5)
B5.pack(ipadx=10,ipady=10)

FB6 = Frame(GUI)
FB6.place(x=420,y=350)
imgPoop6 = PhotoImage(file=picPoop6)
B6 = ttk.Button(FB6,image=imgPoop6,command=popup_Poop6)
B6.pack(ipadx=10,ipady=10)


    
# -- LEFT Section --
L2 = Label(GUI,text="Log",font=("Arial Bold", 50))
L2.place(x=700,y=40)

listShowdata = Frame(GUI)
listShowdata.place(x=700,y=150)

scrollbar = Scrollbar(listShowdata)
scrollbar.pack( side = RIGHT, fill = Y )


mylist = Listbox(listShowdata, yscrollcommand = scrollbar.set, width = 50,bg = "white" )
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

displayCSV()




# -------------------------
# Start the main event loop
GUI.mainloop()
