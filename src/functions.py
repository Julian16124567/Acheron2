import sys
import time

asciiName = r"""

                 ___        __                        
                /   | _____/ /_  ___  _________  ____ 
               / /| |/ ___/ __ \/ _ \/ ___/ __ \/ __ \
              / ___ / /__/ / / /  __/ /  / /_/ / / / /
             /_/  |_\___/_/ /_/\___/_/   \____/_/ /_/ 
           <=========================================>

"""

def drawMain():
    print("\033[95m" + asciiName + "\033[0m")
    print("\n\n")

def animateText(text, amount):
    loading = ["", ".", "..", "..."] 
    color = "\033[95m"  
    reset = "\033[0m"
    for i in range(amount):
        for frame in loading:
            sys.stdout.write(f"\r{color}[*] {text}{frame}{reset}   ")
            sys.stdout.flush()
            time.sleep(0.4)
    print()

def checkWrite(fileCheck):
    with open(f"{fileCheck}", "w") as file:
        inhalt = file.read()
        if len(inhalt) == 0:
            file.close()
            return False
        else:
            return True

def writeCredentials(file_name, inp_file):
    with open(f"{file_name}", "w") as file:
        file.write(inp_file)
        file.close()

def getCredentials(text):
    text = input("\033[36m[*] {text}:\n\033[0m").strip()
    return text

def writeError(e):
    with open("../errorlog/log.txt", "w") as file:
        message = f"[*] {e}"
        file.write(message)
        file.flush()
        file.close()
