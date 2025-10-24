import smtplib
import time
import random
from email.mime.text import MIMEText
from email.header import Header
from colorama import Fore, Style, init
from pyfiglet import Figlet
import sys
import subprocess
import functions 

#print ascii art in color green 
print("\033[36m" + functions.ascii_art + "\033[0m")

#header
figlet = Figlet(font='slant')
print(Fore.CYAN + figlet.renderText("Mail Spammer"))
print("\033[36m" + functions.line + "\033[0m")

#loading animation
def loading(msg, seconds=2):
    for i in range(seconds * 2):
        sys.stdout.write(Fore.YELLOW + f"\r{msg}{'.' * (i % 4)}   ")
        sys.stdout.flush()
        time.sleep(0.5)


#main script 
print(Fore.GREEN + "\n[+] Press Enter to Start\n")
inp = input("")

#work window
subprocess.run("clear");
if inp == "":
    subprocess.run("clear", shell=True)
    functions.drawMain()
    functions.animateText("Checking Credentials", 5)
    
    #check if pwd and email are given
    try:
        while True:    
            checke = functions.checkWrite("email.txt")
            if checke == False:
                email = functions.getCredentials("Insert Email adress: ")
                functions.getCredentials("Gmail Adress", "email.txt")
                continue;
            elif checke == True : 
                checkp = functions.checkWrite("pwd.txt", "Auth Token")
                if checkp == False:
                    pwd = functions.getCredentials("Insert OAuth Token: ")
                    functions.getCredentials("Password", "pwd.txt")
                    continue
                break
    except Exception as e:
        print(f"\033[36m[!] {e}\033[0m")
        functions.writeError(e)

print("\033[36m[*] Credentials checked.\n\033[0m")
time.sleep(2)
sys.stdout.write("\033[F")  
sys.stdout.write("\033[K")  
sys.stdout.flush()

#spammer logic
