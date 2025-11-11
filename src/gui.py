import customtkinter as ctk
import tkinter as tk
import functions

#root withdraw
root = ctk.CTk()
root.title("Acheron 2")
#root.geometry("1000x800")
#root.resizable(False, False)
root.withdraw()

def startWindow():
    root.deiconify()

ctk.set_appearance_mode("dark")

tabs = ctk.CTkTabview(root, width=850, height=480)
tabs.pack(pady=10)

tab1 = tabs.add("Spamer")
tab2  = tabs.add("Daten")




