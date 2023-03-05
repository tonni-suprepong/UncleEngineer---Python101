from random import *

from tkinter import *
from tkinter import ttk
from tkinter import messagebox



# --------------------------------
# Main Parameter
# --------------------------------
jackpots_dct = {}       # jackpot info

# --------------------------------
# Function Section
# --------------------------------
# Fundtion to generate jackpots
def generateJackpots():
    
    loterry = {}

    # jackpot for last number
    loterry["JackpotsLastnum"] = randint(0, 9)

    loterry = {
        "loterry1" : {
            "lotNum" : randint(1, 99),
            "prize" : "ถูกรางวัลที่ 1 ได้รับเงินรางวัล 6,000,000"
        },
        "loterry2" : {
            "lotNum" : randint(1, 99),
            "prize" : "ถูกรางวัลที่ 2 ได้รับเงินรางวัล 200,000"
        },
        "loterry3" : {
            "lotNum" : randint(1, 99),
            "prize" : "ถูกรางวัลที่ 3 ได้รับเงินรางวัล 80,000"
        }
    }
    
    #lotery close to jackpot #1
    loterry["loterry1plus"] = {'lotNum': loterry["loterry1"]["lotNum"]+1, 'prize': 'ถูกรางวัล เลขใกล้เคียงรางวัลที่ 1 ด้านบน ได้รับเงินรางวัล 100,000'}
    loterry["loterry1minus"] = {'lotNum': loterry["loterry1"]["lotNum"]-1, 'prize': 'ถูกรางวัล เลขใกล้เคียงรางวัลที่ 1 ด้านล่าง ได้รับเงินรางวัล 100,000'}
 

    return loterry

# Fundtion to SHOW jackpots
def showJackpots():

    showJackpots_txt = ''                       # SHOW all jackpot number

    # EXTRACT lotery number from jackpots's key
    for value in jackpots_dct.values():

        lotNum = value["lotNum"]
        prize = value["prize"]

        showJackpots_txt = showJackpots_txt + str(lotNum) + ' : ' + prize + '\n'

    
    # SHOW jackpot to messagebox
    messagebox.showinfo('Show Jackpots',showJackpots_txt) 


# Function CHECK INPUT : insert number
def checkInsertNumber(checkIsNum):
     if not checkIsNum.isnumeric():
         messagebox.showerror('Show Jackpots','"' + checkIsNum + '" is not a number, please enter number only')

# MAIN Function to check loteries prize
def CheckLotteryResult():

    insertLot_lis = []      # insert numner info
    jackpotsFlag_dct = {}

    jackpotsFlag_dct.clear()
    insertLot_lis.clear()

    jackpotsResult_txt = '' # SHOW result of the insert number after check jackpots

    # Insert number
    # Insert number : GET lotery number from Entry
    checkInsertNumber(entNum1.get())
    checkInsertNumber(entNum2.get())

    insertLot_lis.append(entNum1.get())
    insertLot_lis.append(entNum2.get())


    # Loop running insert lotery to check with jackpots
    for listValue in insertLot_lis:
        #print(listValue)

        # Loop running each key from jackpots
        for key, value in jackpots_dct.items():

            # EXTRACT lotery number from jackpots's key
            chkLotNum = value["lotNum"]
            
            # CHECK insert number with jackpots
            #   yes add to dic
            if int(listValue) == chkLotNum:
                jackpotsFlag_dct[chkLotNum] = value["prize"]
    # 

    # INTERPRET dic to jackpot result

    isJackpot = len(jackpotsFlag_dct)
    #print(jackpotsFlag_dct)

    if isJackpot == 0:
        jackpotsResult_txt = 'เสียใจด้วย ถูกกิน'

    else:
        for key, value in jackpotsFlag_dct.items():
            jackpotsResult_txt = jackpotsResult_txt + 'เลข ' + str(key) + ' ถูก' + value + '\n'

    messagebox.showinfo('Checking Result',jackpotsResult_txt)


# --------------------------------
# GUI Section
# --------------------------------

backgroundColor = "#7EA8BE"
textColor = "white"

main_window = Tk()
main_window.title('Check Lottery')
main_window.geometry('400x300')
main_window.config(bg=backgroundColor)



H1 = Label(main_window, text="Check Lottery",font=("Anupan Bold", 30),bg=backgroundColor,fg=textColor)
H1.grid(row=0,column=0,columnspan=4,sticky="W",padx=50, pady=5)

H2_lottery = Label(main_window, text="Insert 1-99 to check your lottery",font=("Anupan", 14),bg=backgroundColor,fg=textColor)
H2_lottery.grid(row=1,column=0,columnspan=4, sticky="W",padx=50,pady=10)



lblNum1 = Label(main_window, text="Lotery #1",bg=backgroundColor,fg=textColor)
lblNum1.grid(row=2,column=1,sticky="E",padx=5, pady=5)

entNum1= Entry(main_window)
entNum1.grid(row=2,column=2,sticky="W")
#entNum1.focus_set


lblNum2 = Label(main_window, text="Lotery #2",bg=backgroundColor,fg=textColor)
lblNum2.grid(row=3,column=1,sticky="E",padx=5, pady=5)

entNum2= Entry(main_window)
entNum2.grid(row=3,column=2,sticky="W")



B1_submit = ttk.Button(main_window,text="Check Lottery",command= CheckLotteryResult)
B1_submit.grid(row=4,column=1,sticky="E",padx=5, pady=10)




B2_showJackpot = ttk.Button(main_window,text="Show Jackpot",command= showJackpots)
B2_showJackpot.grid(row=4,column=2,sticky="W",padx=5)

# --------------------------------
# Main Program
# --------------------------------
# GET jackpots number from generate jackpots function
jackpots_dct = generateJackpots()








# -------------------------
# Start the main event loop
main_window.mainloop()



