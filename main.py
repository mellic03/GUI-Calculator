from tkinter import *
from tkinter.constants import W, X
from typing import Collection
import globalVar as glob


def pushNum(x):
    glob.tempList.append(x)
    display.config(text=glob.tempList)


def addWorkingNum():

    glob.state = "add"

    calced = 0
    for v in glob.tempList:

        # index position glob.tempList.index(v)  # list length (len(glob.tempList) - 1)
        calced += v * (10**(abs((glob.tempList.index(v) + 1) - len(glob.tempList))))
        print(v * (10**(abs((glob.tempList.index(v) + 1) - len(glob.tempList)))))

    # add calced to working list
    glob.workingList.append(calced)

    # clear temp list
    glob.tempList = []
    
    print(glob.workingList)


def calculate():
    calced = 0
    if (glob.state == "add"):

        addWorkingNum()
        for v in glob.workingList:
            calced += v
    print(calced)


def calcState(state):
    glob.state = state


def calculatorButtons(frame, x, y):
    # 0-3
    button0 = Button(frame, text="0", width=x, height=y, command=lambda : pushNum(0), background="#474747")
    button0.grid(column=1, row=4)
    button1 = Button(frame, text="1", width=x, height=y, command=lambda : pushNum(1), background="#474747")
    button1.grid(column=1, row=3)
    button2 = Button(frame, text="2", width=x, height=y, command=lambda : pushNum(2), background="#474747")
    button2.grid(column=2, row=3)
    button3 = Button(frame, text="3", width=x, height=y, command=lambda : pushNum(3), background="#474747")
    button3.grid(column=3, row=3)

    # 4-6
    button4 = Button(frame, text="4", width=x, height=y, command=lambda : pushNum(4), background="#474747")
    button4.grid(column=1, row=2)
    button5 = Button(frame, text="5", width=x, height=y, command=lambda : pushNum(5), background="#474747")
    button5.grid(column=2, row=2)
    button6 = Button(frame, text="6", width=x, height=y, command=lambda : pushNum(6), background="#474747")
    button6.grid(column=3, row=2)

    # 7-9
    button7 = Button(frame, text="7", width=x, height=y, command=lambda : pushNum(7), background="#474747")
    button7.grid(column=1, row=1)
    button8 = Button(frame, text="8", width=x, height=y, command=lambda : pushNum(8), background="#474747")
    button8.grid(column=2, row=1)
    button9 = Button(frame, text="9", width=x, height=y, command=lambda : pushNum(9), background="#474747")
    button9.grid(column=3, row=1)

    # operators
    ansButton = Button(frame, text="Ans", width=x, height=y, command=lambda : pushNum(0), background="#5d5e5e")
    ansButton.grid(column=5, row=2)

    equalsButton = Button(frame, text="=", width=x, height=y, command=lambda : calculate(), background="#5d5e5e")
    equalsButton.grid(column=5, row=4)

    addButton = Button(frame, text="+", width=x, height=y, command=lambda : addWorkingNum(), background="#5d5e5e")
    addButton.grid(column=4, row=3)

    subtractButton = Button(frame, text="-", width=x, height=y, command=lambda : pushNum(0), background="#5d5e5e")
    subtractButton.grid(column=5, row=3)

    multiplyButton = Button(frame, text="x", width=x, height=y, command=lambda : pushNum(0), background="#5d5e5e")
    multiplyButton.grid(column=4, row=2)

    divideButton = Button(frame, text="/", width=x, height=y, command=lambda : pushNum(0), background="#5d5e5e")
    divideButton.grid(column=5, row=2)


root = Tk()
root.title("Calculator")
root.geometry("500x600-2680+200")
root.configure(background="#1c1c1c")


displayFrame = Frame(root)
displayFrame.pack(expand=True, side="top")
display = Label(displayFrame, text="this should be a number")
display.pack()


gui = Frame(root)
gui.pack(expand=True, side="bottom")

calculatorButtons(gui, 3, 2)


root.mainloop()
