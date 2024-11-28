import sys
import time
from datetime import date
from tkinter import *
import sys

today = date.today()
start = Tk()
start.title('Sierra Framework Launcher B.Build 203B')
lbl = Label(start, text="""SOP102.Runtime.Launch
Determining Paths.....
Starting SierraFramework....
Started succesfully, Please close this window""")
lbl.grid()
start.mainloop()
n = 9
os2 = '''SierraFramework 0.1.1'''
while n == 9:
    binny = Tk()
    binny.title('Main')
    gh = Label(binny, text="""Please Enter the app specific command to launch the app
    Info - ver
    Textpad - write
    Calculator- calc""")
    Cmd= 0
    e3 = entry(Cmd)
    if Cmd == 'shutdown':
        print('Shutting down')
        break
    elif Cmd == 'ver':
        inf = Tk()
        inf.title('SF188')
        lol = Label(inf, text=os2)
        lol.grid()
        inf.mainloop()
    elif Cmd == "reboot":
        print("Restarting...")
        time.sleep(2.0)
        # restart the loop
    elif Cmd == 'write':
        text = input('''textpad
''')
    elif Cmd == 'readme':
        print('''EliteOS™ is an open source project which can be remixed as long as it is not stripped entirely. 
This is a product which requires an install of the software declared on the website of this product.
Specific rights are reserved such as names of commands, call methods etc.
The EliteOS team''')
    elif Cmd == 'commands':
        print('''Available commands here
*ver
*write
*txtv
*shutdown
*readme
*time
*date
*calc
*mlearn
*volc
*opener
*reboot''')
    elif Cmd == 'sysdel':
        print("❌ system crash")
        print('ERROR CODE: USER_INITIATED_DEATH')
        break
    elif Cmd == 'txtv':
        print(text)
    elif Cmd == 'date':
        print(today)
    elif Cmd == 'time':
        print(time.strftime("%I:%M:%S"))
    elif Cmd == "calc":
        operand1 = input('Please enter an operation: ')
        numa = float(input("Please enter the 1st number: "))
        numb = float(input("Please enter the 2nd number: "))
        if operand1 == "Add" or "add" or "ADD" or "Addition" or "ADDITION":
            print(numa + numb)
        elif operand1 == "minus" or "Minus" or "MINUS" or "subtract" or "Subtract" or "SUBTRACT":
            print(numa - numb)
        elif operand1 == "multiply" or "Multiply" or "MULTIPLY" or "multiplication" or "Multiplication" or "MULTIPLICATION":
            print(numa * numb)
        elif operand1 == "divide" or "Divide" or "DIVIDE" or "division" or "Division" or "DIVISION":
            print(numa / numb)
        else:
            print('This math operation does not exist or is not implemented in the program.')
    elif Cmd == "mlearn":
        num1 = int(input('what is the table?'))
        num2 = int(input('what is the multiple?'))
        num2 = num2 + 1
        num3 = 1
        while num3 < num2:
            print(num1, 'x', num3, "=", num1 * num3)
            num3 = num3 + 1
    elif Cmd == "volc":
        h = input('Please enter the name of the shape: ')
        if h == "cuboid":
            length = float(input("What is the length of the cuboid? "))
            width = float(input("What is the width of the cuboid? "))
            height = float(input("What is the height of the cuboid?: "))
            Volume = length * width * height
            print("The Volume of the Cuboid = %.2f" % Volume)
        elif h == "sphere":
            PI = 3.14
            radius = float(input('Please Enter the Radius of the Sphere: '))
            Volume = (4 / 3) * PI * radius * radius * radius
            print(" The Volume of the Sphere = %.2f" % Volume)
        elif h == "cylinder":
            pi = 3.14
            radius = int(input('Enter the radius of the cylinder: '))
            height = int(input('Enter the height of the cylinder: '))
            volume = pi * radius * radius * height
            print(" Volume of the cylinder = ", volume)
        elif h == "cube":
            length = float(input("What is the length of the cube? "))
            Volume = length * length * length
            print("The Volume of the Cube = %.2f" % Volume)
    elif Cmd == "notify":
        print("☑ no new notifications")
    elif Cmd == "opener":
        oppp = input("Mode: ")
        tuy = input('Path: ')
        K = open(tuy)
        print(K.read())
        if oppp == "write":
            K.write(input("Enter text to add to this file: "))
    elif Cmd == 'Defender':
        print('Elite Defender is not available in this release.')
    else:
        print('⚠ Invalid command')
