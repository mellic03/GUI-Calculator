from tkinter import *
import os

from ctypes import *
so_file = "/home/michael/Desktop/code/projects/GUI calculator/mathlib/mathlib.so"
mymath = CDLL(so_file)


import globalVar as glob



def numericButtons(targetWindow):
    # 0-3
    button0 = Button(targetWindow, text="0", command=lambda : pushNum(0))
    button0.grid(column=1, row=4)
    button1 = Button(targetWindow, text="1", command=lambda : pushNum(1))
    button1.grid(column=1, row=3)
    button2 = Button(targetWindow, text="2", command=lambda : pushNum(2))
    button2.grid(column=2, row=3)
    button3 = Button(targetWindow, text="3", command=lambda : pushNum(3))
    button3.grid(column=3, row=3)

    # 4-6
    button4 = Button(targetWindow, text="4", command=lambda : pushNum(4))
    button4.grid(column=1, row=2)
    button5 = Button(targetWindow, text="5", command=lambda : pushNum(5))
    button5.grid(column=2, row=2)
    button6 = Button(targetWindow, text="6", command=lambda : pushNum(6))
    button6.grid(column=3, row=2)

    # 7-9
    button7 = Button(targetWindow, text="7", command=lambda : pushNum(7))
    button7.grid(column=1, row=1)
    button8 = Button(targetWindow, text="8", command=lambda : pushNum(8))
    button8.grid(column=2, row=1)
    button9 = Button(targetWindow, text="9", command=lambda : pushNum(9))
    button9.grid(column=3, row=1)

def operatorButtons(targetWindow):
    # addition
    addButton = Button(targetWindow, text="+")
    addButton.grid(column=4, row=3)

    # equals
    equalsButton = Button(targetWindow, text="=")
    equalsButton.grid(column=5, row=3)


def pushNum(x):
    num1 = x
    print(num1)
    glob.displayNumber = Label(displayFrame, text=num1)

window = Tk()

window.title("The Cumculator")
window.geometry("300x300")
window.resizable(False, False)

frame1 = Frame(window)
frame1.pack(expand=True, padx=50, pady=50)

displayFrame = Frame(window)
displayFrame.pack(anchor="s")


# numeric buttons
numericButtons(frame1)

# operator buttons
operatorButtons(frame1)


# main loop
window.mainloop()

