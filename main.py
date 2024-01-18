import sys
import os
from pystyle import Center
import webbrowser
from src.apiflood import apiflood, checkapi
from src.dnschecker import dns
from src.flood import conflood
from src.ports import sockscan, reqscan 
from src.spoofcon import spoof

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"

logo = f"""{PURPLE}                  _           __     _   
  /\ /\___   __ _| | __ _  /\ \ \___| |_ 
 / //_/ _ \ / _` | |/ _` |/  \/ / _ \ __|
/ __ \ (_) | (_| | | (_| / /\  /  __/ |_ 
\/  \/\___/ \__,_|_|\__,_\_\ \/ \___|\__|
{WHITE}
A Multifunction Web/Api Stresser/Spoofer

{YELLOW}[1]{WHITE} API Stresser\t\t\t{YELLOW}[2]{WHITE} Check API Response
{YELLOW}[3]{WHITE} DNS Lookup\t\t\t\t{YELLOW}[4]{WHITE} IP Stresser
{YELLOW}[5]{WHITE} Portscanner\t\t\t{YELLOW}[6]{WHITE} Connection Spoofer
{YELLOW}[00]{WHITE} Exit\t\t\t\t{YELLOW}[99]{WHITE} Tool Info
"""

# logo = Center.XYCenter(logo)
logo =  Center.XCenter(logo)
logo = Center.YCenter(logo)


file = open(f"src\\fromthedev.txt","w")
file.write("Hello! This tool is coded with love by infamous koala, here are the links:\nGithub: https://github.com/infamouskoala\nYoutube: https://youtube.com/infamouskoala\nThank you so much for using my tool.")
file.close()

os.system("cls || clear")
os.system("title KoalaNet")
print(logo, end="\n")
option = int(input("enter choice: "))

def clear():
    os.system("cls || clear")

def a():
    print(f"{YELLOW}RELAUNCH THE CLIENT TO CLOSE THE PROCESS{WHITE}")

# main
while True:

  if option == 1:
      a()
      url = input(f"{YELLOW}[URL]{WHITE} enter url: ")
      apiflood(url)

  elif option == 2:
      a()
      url = input(f"{YELLOW}[URL]{WHITE} enter url: ")
      checkapi(url)

  elif option == 3:
      a()
      url = input(f"{YELLOW}[URL]{WHITE} enter url: ")
      dns(url)

  elif option == 4:
      a()
      ip = str(input(f"{YELLOW}[IP]{WHITE} enter ip: "))
      port = int(input(f"{YELLOW}[INT: PORT]{WHITE} port: "))
      sleep = float(input(f"{YELLOW}[FLOAT: SLEEP]{WHITE} sleep: "))
      conflood(ip, port, sleep)

  elif option == 5:
      a()
      ip = input(f"{YELLOW}[IP]{WHITE} IP: ")
      s = int(input(f"{YELLOW}[START]{WHITE} STARTPORT: "))
      e = int(input(f"{YELLOW}[END]{WHITE} ENDPORT: "))
      while True:
          nd = input(f"{YELLOW}[PORTSCAN: HOME]{WHITE} requests: 'r' or socket: 's': ")
          help = nd.lower()
          if help == "r":
              open_ports = reqscan(ip, s, e)
              print(f"{PURPLE}[+]{WHITE} Open ports:", open_ports)
          elif help == "s":
              open_ports = sockscan(ip, s, e)
              print(f"{PURPLE}[+]{WHITE} Open ports:", open_ports)
          else:
              print(f"{RED}[ERROR]{WHITE} Invalid choice '{nd}', its either 'r' or 's'.")

  elif option == 6:
      a()
      ip = input(f"{YELLOW}[HOST]{WHITE} Host IP: ")
      port = int(input(f"{YELLOW}[ACCESS]{WHITE} Access Port: "))
      print(f"{RED}[HIJACK]{WHITE} Connecting to host...")
      spoof(ip, port)

  elif option == 99:
      print(f"""Hello this is Koala, Thank you so much for using my tool. Here are the tool links: 
Github: https://github.com/infamouskoala/koalanet
YouTube: https://youtube.com/infamouskoala 
""")
      x = input(f"{GREEN}[LINK]{WHITE} Github/YouTube: ")
      imlonely = x.lower()
      if imlonely == "github":
          webbrowser.open_new_tab("https://github.com/infamouskoala/koalanet")
          print(f"Opened github link in your browser :)")
          input()
      elif imlonely == "youtube":
          webbrowser.open_new_tab("https://youtube.com/infamouskoala")
          print(f"Opened youtube link in your browser :)")
          input()
      else:
          print(f"{RED}[!]{WHITE} Invalid link '{x}', try 'github' or 'youtube'")
          input()
  elif option == 00:
      clear()
      os.system("title Exitting...")
      print(f"press any key to exit")
      input()
      sys.exit()