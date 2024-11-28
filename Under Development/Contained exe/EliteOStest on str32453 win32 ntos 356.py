import sys
import time
from datetime import date
import sys

import playsound

today = date.today ( )
print ( 'Elite.Runtime.Launch' )
print ( 'Determining Paths.....' )
time.sleep ( 6 )
print ( '' )

os2 = ('''The PyDOS Projecy''')
print ( '''Starting EliteOS....''' )
time.sleep ( 5 )
print ( "System started successfully" )
users = [ "admin" , "Daksh" , "user" , """system""" ]
n = 9

pswd = "****"
name = input ( '''username🆔: ''' )
logon = input ( '''password🔑 : ''' )
if logon == pswd and name in users :
    print ( 'Logging on...' )
    time.sleep ( 0.588 )
else :
    print ( "Incorrect Username or Password" )
    print ( "Logging on to guest mode..." )
    name = 'guest'

while n == 9 :
    Cmd = input ( '>>>' )
    if Cmd == 'shutdown' :
        playsound
        print ( 'Shutting down' )
        break
    elif Cmd == 'ver' :
        print ( os2 )
    elif Cmd == "reboot" :
        print ( "Restarting..." )
        time.sleep ( 2.0 )
        # restart the loop
    elif Cmd == 'write' :
        text = input (
            '''textpad
            '''
            )

    elif Cmd == 'commands' :
        print (
            '''Available commands here
            *ver
            *printdev
            *write
            *txtv
            *shutdown
            *time
            *date
            *calc
            *mlearn
            *volc
            *opener
            *reboot'''
            )
    elif Cmd == 'printdev' :
        print ( "This is a sample text" )
    elif Cmd == 'sysdel' :
        print ( "❌ system crash" )
        print ( 'ERROR CODE: USER_INITIATED_DEATH' )
        break
    elif Cmd == 'txtv' :
        print ( text )
    elif Cmd == 'date' :
        print ( today )
    elif Cmd == 'time' :
        print ( time.strftime ( "%I:%M:%S" ) )
    elif Cmd == "virus.lu" :
        u = 0
        while u != 1052.00 :
            print ( '⚠ Invalid command' )
            u += 0.01
    elif Cmd == "calc" :
        operand1 = input ( 'Please enter an operation: ' )
        numa = float ( input ( "Please enter the 1st number: " ) )
        numb = float ( input ( "Please enter the 2nd number: " ) )
        if operand1 == "Add" or "add" or "ADD" or "Addition" or "ADDITION" :
            print ( numa + numb )
        elif operand1 == "minus" or "Minus" or "MINUS" or "subtract" or "Subtract" or "SUBTRACT" :
            print ( numa - numb )
        elif operand1 == "multiply" or "Multiply" or "MULTIPLY" or "multiplication" or "Multiplication" or "MULTIPLICATION" :
            print ( numa * numb )
        elif operand1 == "divide" or "Divide" or "DIVIDE" or "division" or "Division" or "DIVISION" :
            print ( numa / numb )
        else :
            print ( 'This math operation does not exist or is not implemented in the program.' )
    elif Cmd == "mlearn" :
        num1 = int ( input ( 'what is the table?' ) )
        num2 = int ( input ( 'what is the multiple?' ) )
        num2 = num2 + 1
        num3 = 1
        while num3 < num2 :
            print ( num1 , 'x' , num3 , "=" , num1 * num3 )
            num3 = num3 + 1
    elif Cmd == "volc" :
        h = input ( 'Please enter the name of the shape: ' )
        if h == "cuboid" :
            length = float ( input ( "What is the length of the cuboid? " ) )
            width = float ( input ( "What is the width of the cuboid? " ) )
            height = float ( input ( "What is the height of the cuboid?: " ) )
            Volume = length * width * height
            print ( "The Volume of the Cuboid = %.2f" % Volume )
        elif h == "sphere" :
            PI = 3.14
            radius = float ( input ( 'Please Enter the Radius of the Sphere: ' ) )
            Volume = (4 / 3) * PI * radius * radius * radius
            print ( " The Volume of the Sphere = %.2f" % Volume )
        elif h == "cylinder" :
            pi = 3.14
            radius = int ( input ( 'Enter the radius of the cylinder: ' ) )
            height = int ( input ( 'Enter the height of the cylinder: ' ) )
            volume = pi * radius * radius * height
            print ( " Volume of the cylinder = " , volume )
        elif h == "cube" :
            length = float ( input ( "What is the length of the cube? " ) )
            Volume = length * length * length
            print ( "The Volume of the Cube = %.2f" % Volume )
    elif Cmd == "notify" :
        print ( "☑ no new notifications" )
    elif Cmd == "opener" :
        oppp = input ( "Mode: " )
        tuy = input ( 'Path: ' )
        K = open ( tuy )
        print ( K.read ( ) )
        if oppp == "write" :
            K.write ( input ( "Enter text to add to this file: " ) )
    elif Cmd == "id" :
        if name == 'guest' :
            print ( "Username: guest" )
        else :
            print ( "Username = " , name )
            print ( 'Password = ' , pswd )
    else :
        print ( '⚠ Invalid command' )
