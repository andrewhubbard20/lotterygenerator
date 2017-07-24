# Lotto Program by Andrew Hubbard.
import random
from collections import Counter
rawnumbers = list()
allnumbers = list()
amountofentries= 0
firstnumber = list()
secondnumber = list()
winfirst = 0
winsecond = 0

def startprogram():
    print("Welcome to the company lotto program!")
    print("Select from the following options:")
    print("1. Enter a lotto number.")
    print("2. Find the winning lotto number.")
    print("3. Quit the program.")
    selection = 0
    while 1 > selection <3 :
        try:
            selection = int(input("Selection:"))
        except ValueError:
            print("not a number")

    if selection == 1:
        enterlotto()
    if selection == 2:
        computlotto()
    if selection == 3:
        quit()
    else:
        startprogram()

def enterlotto():
    print("Choose your normal lotto numbers, range of 1-69.")
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    powerballchoice = 0
    firstname = input("First name:")
    lastname = input("Last name:")
   #first number input. Returns a valueError and an error message if out of range or non-int
    while 1 > first or 69 < first:
        try:

            first = int(input("Choose the first number:"))
            if first not in range(1, 69):
                raise ValueError
        except ValueError:

            print('That wasn\'t in the number range:')

    #second
    while 1 > second or 69 < second:
        try:

            second = int(input("Choose the second number:"))
            if second not in range(1, 69):
                raise ValueError
        except ValueError:

            print('That wasn\'t in the number range:')

    #third
    while 1 > third or 69 < third:
        try:

            third = int(input("Choose the third number:"))
            if third not in range(1, 69):
                raise ValueError
        except ValueError:

            print('That wasn\'t in the number range:')

    #fourth
    while 1 > fourth or 69 < fourth:
        try:

            fourth = int(input("Choose the fourth number:"))
            if fourth not in range(1, 69):
                raise ValueError
        except ValueError:

            print('That wasn\'t in the number range:')

    #fifth
    while 1 > fifth or 69 < fifth:
        try:

            fifth = int(input("Choose the fifth number:"))
            if fifth not in range(1, 69):
                raise ValueError
        except ValueError:

            print('That wasn\'t in the number range:')

    print("Finally choose a powerball number, range of 1-26.")
    #powerball
    while 1 > powerballchoice or 26 < powerballchoice:
        try:

            powerballchoice = int(input("Choose the powerballchoice number:"))
            if powerballchoice not in range(1, 26):
                raise ValueError
        except ValueError:

            print('That wasn\'t in the number range:')
    print("The current entris are:")
    numentry = [first, second, third, fourth, fifth, powerballchoice]
    fullentry = [firstname,lastname,first,second,third,fourth,fifth,"Powerball:",powerballchoice]

    #add to list of entries
    rawnumbers.append(numentry)
    allnumbers.append(fullentry)
    firstnumber.append(first)
    secondnumber.append(second)
    print("The current entries are:")
    for p in allnumbers:
        print (*p)
    startprogram()

def findfirst():
    if len(firstnumber) > 1:
        #finds the most common number, if no common number, returns 0.
        m = max([k for k,v in Counter(firstnumber).items() if v>1], default =0)
        if m ==0:

            m = random.randrange(1,69)
            return m
        print(m)

        return m
    else:
        m = random.randrange(1,69)
        return m

def findsecond():
    if len(secondnumber) > 1:
        m = max([k for k, v in Counter(secondnumber).items() if v > 1], default = 0)
        if m == 0:

            m = random.randrange(1,69)
            return m
        print(m)
        return m
    else:
        m = random.randrange(1,69)
        return m




#find the winning lotto number and print the winner.
def computlotto():

    #uses methods to find number 1 and 2 using most common number
    # the rest as per the clarifications, are random.
    winfirst=findfirst()
    winsecond=findsecond()
    winthird = random.randrange(1, 69)
    winfourth = random.randrange(1, 69)
    winfifth= random.randrange(1, 69)
    winpowerball = random.randrange(1,26)
    pball = " Powerball:"
    #Requirement documentation stated to simply print the winning number, not the name of the winner,
    # or check to see if such a winner exists
    print(winfirst, winsecond, winthird,winfourth,winfifth,pball, winpowerball)
    quit()


#program init
startprogram()
