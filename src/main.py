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
import gui
import string
import random

#print ascii ar green 
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

#select gui or tui
print("\033[36m[*] Open GUI (1) or TUI (2).\033[0m")
select_ui = int(input("\033[36m[>] \033[0m"))
while True:
    if select_ui == 1:
        gui.startWindow()
        print("\033[36m[*] Starting GUI.\033[0m")
        break;
    elif select_ui == 2:
        break
    else:
        print("\033[36m[*] Invalid Input.\033[0m")
        print(f"{select_ui}")
        print(type(select_ui))
        continue

#main script 
#print(Fore.GREEN + "\n[+] Press Enter to Start")
print("\033[36m[+] Press Enter to Start.\n\033[0m")
inp = input("")

#work window
subprocess.run("clear");
if inp == "":
    subprocess.run("clear", shell=True)
    functions.drawMain()
    functions.animateText("Checking Credentials", 3)
    
    #check if pwd and email are given
    try:
        while True:    
            checke = functions.checkWrite("email.txt")
            if checke == False:
                email = functions.getCredentials(" Email adress", "email.txt")
                functions.writeCredentials("email.txt", email)
                continue;
            elif checke == True : 
                checkp = functions.checkWrite("pwd.txt")
                if checkp == False:
                    pwd = functions.getCredentials("Insert OAuth Token: ", "pwd.txt")
                    functions.writeCredentials("pwd.txt", pwd)
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
try:
    header = functions.getHeader()
    text = functions.getText()    
    mailto = "julian.zotter.01@icloud.com"                 
    amountmails = functions.getAmount()
    me = functions.mailFrom()
    pwd = functions.getPwd()
except Exception as e:
    print(f"Error {e}")


print("\n")
functions.loading("Connecting Email with Gmail SMTP")
print("\n")


#sending messages
if 1 == 1:
    for i in range(amountmails):
        try:

            msg = MIMEText(text, 'plain', 'utf-8')
            id = random.randint(1000, 9999)
            msg['Subject'] = Header(f"{text} [{id}]", 'utf-8')
            msg['From'] = me
            msg['To'] = mailto

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(me, pwd)
            server.sendmail(me, mailto, msg.as_string())
            server.quit()

            print(f"\033[95m[*] All messages sent successfully!\033[0m")

        except Exception as e:
            print(f"\033[95m[!] {e}\033[0m") 
