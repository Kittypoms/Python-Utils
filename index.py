#Title: Index.py
#Description: The menu wireframe, Displays a simple array of funnies
#Author(s): Danny Morris, Yohan Taukoori, Jack Barun
#Date: 05/02/2022
#Usage: "python -i index.py"
#Version: 0.0.1
#====================IMPORTS====================#
import os
import sys
from pathlib import Path
import shutil
from time import sleep
import colorama
from colorama import Fore
#====================INITIATIONS====================#
colorama.init(autoreset=True)

#====================MAIN-MENU====================#
def main_menu():
    print("-" * 20 + Fore.RED + "DJY" + Fore.WHITE + "-" * 20)
    print("1: " + Fore.RED + "Main Menu")
    print("2: " + Fore.YELLOW +"PC Speed")
    print("3: " + Fore.GREEN +"Directories")
    print("4:")
    print("5:")
    print("6:")
    print("7:")
    print("8:")
    print("9: Quit")
    userinput = input(">>> ")
    #====================SUB-MENU-1====================#
    if userinput == "1":
        clear = lambda: os.system('cls')
        clear()
        main_menu()
    if userinput == "2":
        print("hi")
    #====================PC SPEED====================#
    if userinput == "2":
        tempsize = os.path.getsize('C:\Windows\Temp')
        print("-" * 20 + "DIRECTORIES" + "-" * 20)
        print("1: Main Menu")
        print("2: Clear Recycle Bin")
        print("3: Open Temp Files.     --" + str(tempsize) + "kb of data will be removed.")
        print("4:")
        print("5:")
        print("6:")
        print("7:")
        print("8:")
        print("9: Quit")
        menu2input = input(">>> ")
        if menu2input == "1":
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu2input == "3":
            print("!Delete The Files in This Directory!")
            for x in range (0,5):  
                b = "Loading" + "." * x
                print (b, end="\r")
                sleep(0.1)
            temp_path = str("C:\\Windows\\Temp")
            os.startfile(temp_path)
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu2input == "9":                                                       
            exit(0)
    #====================DIRECTORIES====================#
    if userinput == "3":
        print("-" * 20 + "DIRECTORIES" + "-" * 20)
        print("1: Main Menu")
        print("2: Downloads")
        print("3: Appdata")
        print("4: Minecraft Mods")
        print("5: Obs Captures")
        print("6: Desktop")
        print("7:")
        print("8:")
        print("9: Quit")
        menu3input = input(">>> ")
        if menu3input == "1":
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu3input == "2":
            downloads_path = str(Path.home() / "Downloads")
            os.startfile(downloads_path)
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu3input == "3":
            appdata_path = str(Path.home() / "AppData")
            os.startfile(appdata_path)
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu3input == "4":
            mcmods_path = str(Path.home() / "AppData/Roaming/.minecraft/Mods")
            os.startfile(mcmods_path)
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu3input == "5":
            obscaptures_path = str(Path.home() / "Videos/Captures")
            os.startfile(obscaptures_path)
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu3input == "4":
            desktop_path = str(Path.home() / "OneDrive/Desktop")
            os.startfile(desktop_path)
            clear = lambda: os.system('cls')
            clear()
            main_menu()
        if menu3input == "9":
            exit(0)
    if userinput == "9":
        exit(0)

main_menu()

