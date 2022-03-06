import os
workingPath = os.path.dirname(__file__)

# C math library
#from ctypes import *
#so_file = workingPath + "/mathlib/mathlib.so"
#mathlib = CDLL(so_file)


from tkinter import *
import globalVar as glob


class Calculator():
    def __init__(self, frame, display):
        self.frame = frame
        self.display = display
        
    def draw(self, width, height):
        # 0-3
        button0 = Button(self.frame, text="0", width=width, height=height, command=lambda : self.pushDigitToDisplay(0), background="#474747")
        button0.grid(column=1, row=4)
        button1 = Button(self.frame, text="1", width=width, height=height, command=lambda : self.pushDigitToDisplay(1), background="#474747")
        button1.grid(column=1, row=3)
        button2 = Button(self.frame, text="2", width=width, height=height, command=lambda : self.pushDigitToDisplay(2), background="#474747")
        button2.grid(column=2, row=3)
        button3 = Button(self.frame, text="3", width=width, height=height, command=lambda : self.pushDigitToDisplay(3), background="#474747")
        button3.grid(column=3, row=3)

        # 4-6
        button4 = Button(self.frame, text="4", width=width, height=height, command=lambda : self.pushDigitToDisplay(4), background="#474747")
        button4.grid(column=1, row=2)
        button5 = Button(self.frame, text="5", width=width, height=height, command=lambda : self.pushDigitToDisplay(5), background="#474747")
        button5.grid(column=2, row=2)
        button6 = Button(self.frame, text="6", width=width, height=height, command=lambda : self.pushDigitToDisplay(6), background="#474747")
        button6.grid(column=3, row=2)

        # 7-9
        button7 = Button(self.frame, text="7", width=width, height=height, command=lambda : self.pushDigitToDisplay(7), background="#474747")
        button7.grid(column=1, row=1)
        button8 = Button(self.frame, text="8", width=width, height=height, command=lambda : self.pushDigitToDisplay(8), background="#474747")
        button8.grid(column=2, row=1)
        button9 = Button(self.frame, text="9", width=width, height=height, command=lambda : self.pushDigitToDisplay(9), background="#474747")
        button9.grid(column=3, row=1)

        # decimal
        decimalButton = Button(self.frame, text=".", width=width, height=height, command=lambda : self.pushDigitToDisplay("."), background="#5d5e5e")
        decimalButton.grid(column=4, row=4)

        # parentheses
        openParenthesisButton = Button(self.frame, text="(", width=width, height=height, command=lambda : self.pushDigitToDisplay("("), background="#5d5e5e")
        openParenthesisButton.grid(column=2, row=4)

        closedParenthesisButton = Button(self.frame, text=")", width=width, height=height, command=lambda : self.pushDigitToDisplay(")"), background="#5d5e5e")
        closedParenthesisButton.grid(column=3, row=4)

        # operators
        ansButton = Button(self.frame, text="Ans", width=width, height=height, command=lambda : self.pushDigitToDisplay(0), background="#5d5e5e")
        ansButton.grid(column=5, row=2)

        equalsButton = Button(self.frame, text="=", width=width, height=height, command=lambda : self.calculate(), background="#5d5e5e")
        equalsButton.grid(column=5, row=4)

        addButton = Button(self.frame, text="+", width=width, height=height, command=lambda : self.pushDigitToDisplay("+"), background="#5d5e5e")
        addButton.grid(column=4, row=3)

        subtractButton = Button(self.frame, text="-", width=width, height=height, command=lambda : self.pushDigitToDisplay("-"), background="#5d5e5e")
        subtractButton.grid(column=5, row=3)

        multiplyButton = Button(self.frame, text="x", width=width, height=height, command=lambda : self.pushDigitToDisplay("*"), background="#5d5e5e")
        multiplyButton.grid(column=4, row=2)

        divideButton = Button(self.frame, text="/", width=width, height=height, command=lambda : self.pushDigitToDisplay("/"), background="#5d5e5e")
        divideButton.grid(column=5, row=2)

        clearButton = Button(self.frame, text="CLEAR", width=width, height=height, command=lambda : self.clearCalculator(), background="#5d5e5e")
        clearButton.grid(column=5, row=1)
        
        backSpaceButton = Button(self.frame, text="BKSP", width=width, height=height, command=lambda : self.backSpace(), background="#5d5e5e")
        backSpaceButton.grid(column=4, row=1)

        factorialButton = Button(self.frame, text="!", width=width, height=height, command=lambda : self.backSpace(), background="#5d5e5e")
        factorialButton.grid(column=6, row=1)

    def refreshText(self, textBox, OPTION):
        if (OPTION == "refresh"):
            textBox.config(text = glob.displayList)
        elif (OPTION == "reset"):
            glob.displayList = []


    def pushDigitToDisplay(self, x):
        # if the reset switch is on and the user presses a non-numeric buton
        if (glob.resetTrigger):
            try:
                intTest = float(x)
                # x is numeric
                self.refreshText(self.display, "reset")

            except:
                pass

            glob.resetTrigger = False

        glob.displayList.append(str(x))
        self.refreshText(self.display, "refresh")


    def calculate(self):

        # evaluate
        expression = "".join(glob.displayList)
        result = eval(expression)

        # display result
        self.refreshText(self.display, "reset")
        self.pushDigitToDisplay(result)
        
        # turn reset switch on in case user next presses a number instead of an operator
        glob.resetTrigger = True


    def clearCalculator(self):
        # reset variables
        glob.workingList = [0]
        glob.displayList = []
        glob.sign = 1

        # refresh the display
        self.refreshText(self.display, "refresh")


    def backSpace(self):
        glob.displayList.pop()
        self.refreshText(self.display, "refresh")
