from tkinter import *
from tkinter.constants import W, X
from typing import Collection

import os
workingPath = os.path.dirname(__file__)

# C math library
from ctypes import *
so_file = workingPath + "/mathlib/mathlib.so"
mymath = CDLL(so_file)


import globalVar as glob


def refreshText(textBox, OPTION):
    if (OPTION == "refresh"):
        textBox.config(text = glob.displayList)
    elif (OPTION == "reset"):
        glob.displayList = []


def pushDigitToDisplay(x):
    # push digit to display
    glob.displayList.append(str(x))
    # refresh the display
    refreshText(display, "refresh")


def pushDisplayToWorkingList():
    if glob.displayList:
        # convert displayed string into float and push to glob.workingList
        glob.workingList.append(float("".join(glob.displayList)) * glob.sign)
        # reset the display list
        refreshText(display, "reset")
        print(glob.workingList)


def addNum():
    pushDisplayToWorkingList()
    glob.sign = 1


def subtractNum():
    pushDisplayToWorkingList()
    glob.sign = -1

def multiplyNum():
    glob.state = "multiply"

def divideNum():
    glob.state = "divide"


def calculate():
    pushDisplayToWorkingList()
    glob.sign = 1
    calculation = sum(glob.workingList)
    glob.workingList = [0]
    pushDigitToDisplay(calculation)


def clearCalculator():
    # reset variables
    glob.workingList = [0]
    glob.displayList = []
    glob.sign = 1
    # refresh the display
    refreshText(display, "refresh")


def calculatorButtons(frame, x, y):
    # 0-3
    button0 = Button(frame, text="0", width=x, height=y, command=lambda : pushDigitToDisplay(0), background="#474747")
    button0.grid(column=1, row=4)
    button1 = Button(frame, text="1", width=x, height=y, command=lambda : pushDigitToDisplay(1), background="#474747")
    button1.grid(column=1, row=3)
    button2 = Button(frame, text="2", width=x, height=y, command=lambda : pushDigitToDisplay(2), background="#474747")
    button2.grid(column=2, row=3)
    button3 = Button(frame, text="3", width=x, height=y, command=lambda : pushDigitToDisplay(3), background="#474747")
    button3.grid(column=3, row=3)

    # 4-6
    button4 = Button(frame, text="4", width=x, height=y, command=lambda : pushDigitToDisplay(4), background="#474747")
    button4.grid(column=1, row=2)
    button5 = Button(frame, text="5", width=x, height=y, command=lambda : pushDigitToDisplay(5), background="#474747")
    button5.grid(column=2, row=2)
    button6 = Button(frame, text="6", width=x, height=y, command=lambda : pushDigitToDisplay(6), background="#474747")
    button6.grid(column=3, row=2)

    # 7-9
    button7 = Button(frame, text="7", width=x, height=y, command=lambda : pushDigitToDisplay(7), background="#474747")
    button7.grid(column=1, row=1)
    button8 = Button(frame, text="8", width=x, height=y, command=lambda : pushDigitToDisplay(8), background="#474747")
    button8.grid(column=2, row=1)
    button9 = Button(frame, text="9", width=x, height=y, command=lambda : pushDigitToDisplay(9), background="#474747")
    button9.grid(column=3, row=1)

    # operators
    ansButton = Button(frame, text="Ans", width=x, height=y, command=lambda : pushDigitToDisplay(0), background="#5d5e5e")
    ansButton.grid(column=5, row=2)

    equalsButton = Button(frame, text="=", width=x, height=y, command=lambda : calculate(), background="#5d5e5e")
    equalsButton.grid(column=5, row=4)

    addButton = Button(frame, text="+", width=x, height=y, command=lambda : addNum(), background="#5d5e5e")
    addButton.grid(column=4, row=3)

    subtractButton = Button(frame, text="-", width=x, height=y, command=lambda : subtractNum(), background="#5d5e5e")
    subtractButton.grid(column=5, row=3)

    multiplyButton = Button(frame, text="x", width=x, height=y, command=lambda : multiplyNum(), background="#5d5e5e")
    multiplyButton.grid(column=4, row=2)

    divideButton = Button(frame, text="/", width=x, height=y, command=lambda : divideNum(), background="#5d5e5e")
    divideButton.grid(column=5, row=2)

    clearButton = Button(frame, text="CLEAR", width=x, height=y, command=lambda : clearCalculator(), background="#5d5e5e")
    clearButton.grid(column=5, row=1)


root = Tk()
root.title("Calculator")
root.geometry("500x600")#-2680+200")
root.configure(background="#1c1c1c")


displayFrame = Frame(root)
displayFrame.pack(expand=True, side="top")
#display = Label(displayFrame, text="this should be a number")
display = Label(displayFrame, text = "Nothing yet")
display.pack()


gui = Frame(root)
gui.pack(expand=True, side="bottom")

calculatorButtons(gui, 4, 2)


root.mainloop()
