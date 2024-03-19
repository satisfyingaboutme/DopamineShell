import os
import subprocess
import platform
import json
import shutil
from modules.utils import *
from modules.dopahelper import *

def print_intro(palette_data):
    r1 = palette_data.get("r1", 255)
    g1 = palette_data.get("g1", 217)
    b1 = palette_data.get("b1", 0)
    r2 = palette_data.get("r2", 0)
    g2 = palette_data.get("g2", 255)
    b2 = palette_data.get("b2", 98)

    Clean()
    cLogo("cygnet", " Dopamine", r1, g1, b1, r2, g2, b2)
    ePrint("  Modded shell for Termux and Fedora/etc.", r1, g1, b1, r2, g2, b2)
    ePrint("  Made by @sounz1x for him/public use", r1, g1, b1, r2, g2, b2)
    ePrint("  Version: AplhaTest1.1", r1, g1, b1, r2, g2, b2)
    Empty()

def change_directory(args):
    if args:
        try:
            os.chdir(args[0])
        except FileNotFoundError:
            print("  No such directory:", args[0])
    else:
        print("  No directory specified in arguments")

def format_output(output):
    lines = output.split('\n')
    formatted_output = ''
    for line in lines:
        if line.strip():
            formatted_output += '  ' + line.strip() + ''
    return formatted_output

def execute_command(command):
    
    if shutil.which(command) is None:
        print(f"  Command {command} not found.")
    else:
        try:
            os.system(command)
            output = subprocess.check_output(command, shell=True, text=True)
            formatted_output = format_output(output)
            print(formatted_output.rstrip('\n'))
        except subprocess.CalledProcessError as e:
            j = e
    	
def dopafetch():
    print("  ┌─────────────────────────────────────────────────────┐")
    print("  │                   System Information                │")
    print("  ├─────────────────────────────────────────────────────┤")
    print(f" │ OS: {platform.system()} {platform.release():<30}    │")
    print(f" │ Python Version: {platform.python_version():<30}     │")
    print(f" │ Processor: {platform.processor():<35}               │")
    print(f" │ Machine: {platform.machine():<37}                   │")
    print(f" │ Node: {platform.node():<39}                         │")
    print("  └─────────────────────────────────────────────────────┘")

def neofetch():
    print("  neofetch is not available. Consider using dopafetch instead:")

def display_help():
    print("  Available commands:")
    print("    cd <directory>: Change current directory")
    print("    ls, dir, pwd: List directory contents")
    print("    apt-get <arguments>: Package manager for installing, updating, and removing software")
    print("    dopafetch: Display system information")
    print("    neofetch: Display system information (alternative to dopafetch)")
    print("    exit: Exit the shell")
    print("    help: Display this help message")
    print("    basic linux commands: <none>")

def abort(pname, palette_data):
    r1 = palette_data.get("r1", 255)
    g1 = palette_data.get("g1", 217)
    b1 = palette_data.get("b1", 0)
    r2 = palette_data.get("r2", 0)
    g2 = palette_data.get("g2", 255)
    b2 = palette_data.get("b2", 98)
    
    while True:
        console = input(f"  {pname}@{gethost()}:{getcurrentdir()}$ ")
        command, *args = console.split()

        try:
            if command == "cd":
                change_directory(args)
            elif command in ["ls", "dir", "pwd"]:
                execute_command(console)
            elif command in ["restart", "update"]:
                os.system("python3 ./main.py")
            elif command == "apt":
                execute_command("apt-get")
            elif command == "help":
                display_help()
            elif command == "dopafetch":
                dopafetch()
            elif command == "neofetch":
                neofetch()
            elif command in ["exit", "quit", "kill"]:
                ePrint("  Exiting...", r1, g1, b1, r2, g2, b2)
                break
            else:
                execute_command(console)
        except KeyboardInterrupt:
            ePrint("\n  Shutdown!", r1, g1, b1, r2, g2, b2)
            break

def load_palette():
    try:
        with open("palette.json", "r") as file:
            palette_data = json.load(file)
        return palette_data
    except FileNotFoundError:
        print("Palette file not found. Using default values.")
        return None

def main():
    pname = "dopamine"
    palette_data = load_palette()
    if palette_data:
        print_intro(palette_data)
    else:
        print_intro({})
    abort(pname, palette_data)

if __name__ == "__main__":
    main()
