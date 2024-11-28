import time
import os
import hashlib
import magic
import pyfiglet
import requests 
from datetime import date
import platform
today = date.today()
os2 = ('''SierraDOS 1 X86
 All rights reserved''')
print('''Starting SierraDOS....''')
time.sleep(5)
print("System started successfully")
users = ["admin" , "Daksh"]
n = 9
pswd = "****"
name = input('''username🆔: ''')
logon = input('''password🔑 : ''')
if logon == pswd and name in users:
    print('Logging on...')
    time.sleep(0.588)
else:
    print("Incorrect Username or Password")
while n == 9:
    if logon != pswd:
        print("⚠ Incorrect Password")
        print("❕ system terminated")
        break
    Cmd = input('>>>')
    if Cmd == 'shutdown':
        print('Shutting down')
        break
    elif Cmd == 'ver':
        print(os2)
    elif Cmd == 'write':
        text = input('''textpad
''')
    elif Cmd == 'readme':
        print('''SierraDOS™ is a beta OS and not intended for commercial use and also not released  yet. 
More commands will be added later .All system and test files are copyrighted by Sierra Computer Co. .All rights reserved''')
    elif Cmd == 'commands':
        print('''Available commands here
*ver
*printdev
*write
*txtv
*shutdown
*readme
*updates
*OSc
*time
*date
*kernelu
*calc
*mlearn
*volc''')
    elif Cmd == 'system dirs':
        print('''
ELITESYSAPPS.fl💻🗝
BOOT.fl 🗝
CLOCK.app
INFO.app
LOGINUI.ui💻🗝
OS.sys.imp.drive.img💻🗝
Help.app
WESYSTEM.fl💻🗝
ELITEUTIL.fl💻🗝
IMPORTANT SYSTEM.fl💻🗝
Updatetool.msci💻🗝''')
    elif Cmd == 'kerneli':
        ger = "Python"
        print(ger)
    elif Cmd == 'runtime':
        mz = "Py3.5 "
        print(mz)
    elif Cmd == 'printdev':
        print("This is a sample text")
    elif Cmd == 'sysi':
        print('''System information
Storage = 
RAM = 8 GB
Processor = Intel® core i5
Processor speed = 2.50 GHz
OS compatibility  ✅''')
    elif Cmd == 'sysdel':
        playsound('crash.wav')
        print("❌ system crash")
        print('⚠ WESYSTEM.fl was not found')
        break
    elif Cmd == 'updates':
        print('Checking for updates please wait...')
        time.sleep(1.0)
        print('1 Update found')
        clan = """SierraDOS 1.1 x64
All rights reserved"""
        os2 = clan
        des = input('Do you want to update to SierraDOS 1.1? ')
        if des == 'yes' or 'YES' or 'Yes':
            print('Verifying Update')
            time.sleep(2.5)
            print('Updating software...')
            time.sleep(10.2)
            print("Writing older OS backup to the disk...")
            time.sleep(5.88)
            print('Finishing Update...')
            time.sleep(4.5)
            print('SierraDOS has been updated successfully. You have been logged on.')
            continue
        elif des == "no" or "NO" or "No" or "nO":
            print('update ignored')
    elif Cmd == 'OSc':
       my_pc = platform.uname()
       print(f"Operating System: {my_pc.system}")
       print(f"Node Name: {my_pc.node}")
       print(f"Release: {my_pc.release}")
       print(f"Version: {my_pc.version}")
       print(f"Machine: {my_pc.machine}")
       print(f"Processor: {my_pc.processor}")
       print(f"Architecture: {platform.architecture}")
    elif Cmd == 'reset':
        des3 = input("Do you want to reset SierraDOS ?")
        if des3 == 'yes' or 'YES' or 'Yes':
            print('resetting sierraDOS...')
            print('removing install...')
            time.sleep(18.14)
            print('reinstalling RIAD 5.4...')
            time.sleep(20.3)
            print('reinstalling Apps and utilities...')
            time.sleep(9.2)
            print('reinstalling OS.img...')
            time.sleep(13.2)
            print('Shutting down...')
            break
    elif Cmd == 'txtv':
        print(text)
    elif Cmd == 'date':
        print(today)
    elif Cmd == 'time':
        print(time.strftime("%I:%M:%S"))
    elif Cmd == "kernelu":
        print('Checking for kernel updates...')
        time.sleep(0.5)
        print('1 update available')
        ve = 'SierraDOS_DEV 5.3'
        ger = ve
        print(ve)
        print("preparing to update...")
        time.sleep(7.1)
        print('OS has entered Low Functionality mode')
        print("Installing updates...")
        time.sleep(10.3)
        print('Updated successfully')
        print(' OS is exiting Low Functionality mode')
        time.sleep(1)
        continue
    elif Cmd == "OSi":
        print('Experience index 🔟')
        print('''* Displaying items 🔟
* HDD proccess         🔟
* RAM                  🔟
''')
    elif Cmd == "virus.lu":
        u = 0
        while u != 1052.00:
            print('⚠ Invalid command')
            u += 0.01
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
            width = float(input("What is the width of the cube? "))
            height = float(input("What is the height of the cube? "))
            Volume = length * width * height
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
    elif Cmd == "id":
        print("Username = " , name)
        print('Password = ' , pswd)
    else:
        print('⚠ Invalid command')

