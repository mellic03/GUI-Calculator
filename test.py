import os
workingPath = os.path.dirname(__file__)

# C math library
from ctypes import *
so_file = workingPath + "/mathlib/mathlib.so"
mathlib = CDLL(so_file)


listToEval = ["15", "+", "5", "+", "5!"]

def computeFactorial():

    workingList = []

    for char in targetString:
        
        # if the character is not "!", push the number to workinglist
        if (char != "!"):
            x = int(char)
            workingList.append(char)

        # if the character is "!", append value as factorial(value)
        elif (char == "!"):
            targetList[targetList.index(targetString)] = mathlib.factorial(int("".join(workingList)))


def find(x):
            return {
                "!": computeFactorial(),
                "+": print("Plussu"),
                "c": 3,
            }.get(x, "none")


def computeExpression(targetList):

    # loop through each string in the list
    for string in targetList:

        # loop through each character in the string
        for char in string:

            # check each character to determine if it is an operator
            computedString = find(char, targetList, string)
            




computeExpression(listToEval)