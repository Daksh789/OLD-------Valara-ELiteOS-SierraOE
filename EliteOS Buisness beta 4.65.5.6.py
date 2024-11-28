
from datetime import date
import PySimpleGUI as sg
today = date.today()
from playsound import playsound
import time
sg.theme('DarkAmber')
os2 = ('''EliteOS™ beta 4.65.5 x64 
 All rights reserved™''')
print(' starting EliteOS beta 4 ')
print(' started successfully')
n = 9
pswd = 'windows7'
logon = input('''password🔑 : ''')
if logon == pswd:
    print('✅ Correct Password')
while n == 9:
    while logon != pswd:
        playsound("chord.wav")
        print("⚠ Incorrect Password")
        logon = input('''password🔑 : ''')


    Cmd = input('>>>')

    if Cmd == 'shutdown':

        playsound('powerd.wav')
        print('Shutting down')
        break
    elif Cmd == 'ver':
        sg.Window(os2)
        sg.Button("ok")
    elif Cmd == 'write':
        text = input('''textpad
''')
    elif Cmd == 'readme':
        print('''EliteOS™ is a beta OS and not intended for commercial use and also not released  yet. 
More commands will be added later .All system and test files are copyrighted by Elite software©.All rights reserved''')
    elif Cmd == 'commands':
        print('''Available commands here
*ver
*printdev
*write
*txtv
*shutdown
*readme
*system dirs
*kerneli
*runtime
*sysi
*updates
*health
*OSc
*protect
*protecti
*protectu
*errors1
*errors2
*time
*date
*media''')
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
        print("Elite_DEV  6.2 ")
    elif Cmd == 'runtime':
        print("NT 10.00 Elite overbase 3.5 ")
    elif Cmd == 'printdev':
        print("This is a sample text")
    elif Cmd == 'sysi':
        print('''System information
PC model = Optiplex 7040
PC manufacturer = DELL
Storage = 500 GB
RAM = 8 GB
Processor = Intel® core i5
Processor speed = 2.50 GHz
OS compatibility  ✅''')
    elif Cmd == 'sysdel':
        playsound('crash.wav')
        sg.Window("❌ system crash")

        break
    elif Cmd == 'health':
        print('''syshealth utility
checking PC health
*Processor ✅
*RAM ✅
*Hard Disk ✅
*GPU ✅
*Keyboard ✅
*Port1 ✅
*Port2 ✅
*usbA ✅
*usbB ✅
*Audio ✅
*GPU ✅''')
    elif Cmd == 'updates':
        print('Checking for updates please wait...')
        print('1 Update found')
        des = input('do you want to update to EliteOS beta 4.65.5? ')
        if des == 'yes' or 'YES' or 'Yes':
            print('Updating software...')

            continue
        else:
            print('update ignored')

