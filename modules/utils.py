import os
import json
from art import *
from rgbprint import *
import time

def load_palette():
    try:
        with open("palette.json", "r") as file:
            palette_data = json.load(file)
        return palette_data
    except FileNotFoundError:
        print("Palette file not found. Using default values.")
        return None

def save_palette(palette_data):
    with open("palette.json", "w") as file:
        json.dump(palette_data, file)
    print("Palette saved successfully.")

def palette_change(args, r1, g1, b1, r2, g2, b2):
    if len(args) == 6:
        try:
            r1, g1, b1, r2, g2, b2 = map(int, args)
            print("Palette updated successfully.")
            palette_data = {
                "r1": r1,
                "g1": g1,
                "b1": b1,
                "r2": r2,
                "g2": g2,
                "b2": b2
            }
            save_palette(palette_data)
            return r1, g1, b1, r2, g2, b2
        except ValueError:
            print("Invalid input. Please provide 6 integer values for r1, g1, b1, r2, g2, b2.")
    else:
        print("Invalid number of arguments. Please provide 6 integer values for r1, g1, b1, r2, g2, b2.")
    return r1, g1, b1, r2, g2, b2

def Sleep(int):
    time.sleep(int)

def Clean():
    os.system("clear")

def Empty():
    print()

def cLogo(font, text, r1, g1, b1, r2, g2, b2):
    logo_super = text2art(text, font=font)
    gradient_print(logo_super, start_color=Color(r1, g1, b1), end_color=Color(r2, g2, b2))

def cMenuW(text, usr, r1, g1, b1, r2, g2, b2):
    print()
    gradient_print(" [#] " + text + usr + ".", start_color=Color(r1, g1, b1), end_color=Color(r2, g2, b2))

def cMenu(text, r1, g1, b1, r2, g2, b2):
    print()
    gradient_print(" [#] " + text, start_color=Color(r1, g1, b1), end_color=Color(r2, g2, b2))

def cList(int, text, r1, g1, b1, r2, g2, b2):
    gradient_print(" ["+int+"] "+text, start_color=Color(r1, g1, b1), end_color=Color(r2, g2, b2))

def ePrint(text, r1, g1, b1, r2, g2, b2):
    gradient_print(text, start_color=Color(r1, g1, b1), end_color=Color(r2, g2, b2))

def eFixPrint(text, r1, g1, b1, r2, g2, b2):
    return "gradient_print(text, start_color=Color(r1, g1, b1), end_color=Color(r2, g2, b2))"

def cPrint(colr, colr2, text):
    gradient_print(text, start_color=colr, end_color=colr2)

def Inf():
    st = input(" ")
    
    if st == "exit":
        os.system("python3 ./main.py")
    else:
        Inf()

def main():
    palette_data = load_palette()
    if palette_data:
        r1, g1, b1, r2, g2, b2 = palette_data["r1"], palette_data["g1"], palette_data["b1"], palette_data["r2"], palette_data["g2"], palette_data["b2"]
    else:
        r1, g1, b1, r2, g2, b2 = 255, 217, 0, 0, 255, 98

    while True:
        console = input("palette$ ")
        command, *args = console.split()

        if command == "change":
            r1, g1, b1, r2, g2, b2 = palette_change(args, r1, g1, b1, r2, g2, b2)
        elif command == "save":
            palette_data = {
                "r1": r1,
                "g1": g1,
                "b1": b1,
                "r2": r2,
                "g2": g2,
                "b2": b2
            }
            save_palette(palette_data)
        elif command == "load":
            palette_data = load_palette()
            if palette_data:
                r1, g1, b1, r2, g2, b2 = palette_data["r1"], palette_data["g1"], palette_data["b1"], palette_data["r2"], palette_data["g2"], palette_data["b2"]
        elif command == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Available commands: change, save, load, exit")

if __name__ == "__main__":
    main()
