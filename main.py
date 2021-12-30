from tkinter import *
from tkinter.constants import W, X
import calculator

root = Tk()
root.title("Calculator")
root.geometry("275x300")#-2680+200")
root.configure(background="#1c1c1c")


displayFrame = Frame(root)
displayFrame.pack(expand=True, side="top")

digitDisplay = Label(displayFrame, text = "Nothing yet")
digitDisplay.config(font=("Courier", 20))
digitDisplay.pack()


gui = Frame(root)
gui.pack(expand=True, side="bottom")

calculatorButtons = calculator.Calculator(gui, digitDisplay)
calculatorButtons.draw(3, 2)


root.mainloop()