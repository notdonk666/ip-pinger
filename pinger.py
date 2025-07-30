from os import system   # for clearing the screen
import platform         # for identifying os
import subprocess       # for running other commands example ping

# ANSI color codes
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"

# platform check to make program cross platform
if platform.system().lower() == 'windows':
    clear = 'cls'
else:
    clear = 'clear'

# whats point of a tool if u dont have ascii???
ascii = (r"""
    
    ██╗██████╗       ██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗ 
    ██║██╔══██╗      ██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗
    ██║██████╔╝█████╗██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
    ██║██╔═══╝ ╚════╝██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
    ██║██║           ██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
    ╚═╝╚═╝           ╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                   
    
    """)

def ping(host):
    # diff command for diff OS
    if platform.system().lower() == 'windows':
        param = '-n'
    else:
        param = '-c'
    command = ['ping', param, '1', host] # command for the ping

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # subprocess.run - runs the command we give it
        # stdout=subprocess.PIPE - stores the success msg
        # stderr=subprocess.PIPE - stores the error msg
        return result.returncode == 0 # returns 0 [success] if no issues
    
    except Exception:
        return False # return false [error] if there is a issue

# main program
while True:
    system(clear) # clears screen
    print(ascii) # print our 10/10 ascii
    print(f"{GREEN}[!] select an option :{RESET}\n")
    print(f"{YELLOW}[1] start pinger{RESET}")
    print(f"{YELLOW}[2] exit{RESET}\n")

    opt = input(f"{YELLOW}[>] {RESET}")

    if opt == "1": # 
        system(clear)
        print(f"{GREEN}[!] enter ip :{RESET}")
        ip = input(f"{YELLOW}[>] {RESET}") # getting ip by user

        print(f"{GREEN}[!] pinging {ip} ...{RESET}")

        if ping(ip): # using our function to check if ip is reachable
            print(f"{GREEN}[+] {ip} is reachable!{RESET}")
        else:
            print(f"{RED}[-] {ip} is not reachable.{RESET}")

        input(f"\n{YELLOW}Press Enter to continue...{RESET}")

    elif opt == "2": # breaks out of while loop if user exits
        break
