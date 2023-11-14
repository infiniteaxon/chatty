import socket
import random
from datetime import datetime
from threading import Thread
from colorama import Fore, init

init()  # Colorama
colors = [Fore.BLUE, Fore.LIGHTBLUE_EX, Fore.CYAN, Fore.LIGHTCYAN_EX,
          Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.RED, Fore.LIGHTRED_EX,
          Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, Fore.YELLOW, Fore.LIGHTYELLOW_EX,
          Fore.WHITE]

uCOLOR = random.choice(colors)  # Picks random color for each client

sHOST = "10.7.1.2"  # Server IP
sPORT = 2003  # Server Port
sep = "<SEP>"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Initialize TCP socket
print(f"[*] Connecting to {sHOST}:{sPORT}...")  # Return status

tcp.connect((sHOST, sPORT))  # Connect to server
print("[+] Connected.")  # Return status

name = input("Enter your name: ")  # Client inputs username


def listen():  # Function to listen for messages
    while True:
        message = tcp.recv(1024).decode()  # When message is received
        print("\n" + message)  # Print message


t = Thread(target=listen)  # Listen for messages always
t.daemon = True  # Daemon wil end threads when main ends
t.start()  # Start thread

while True:
    sending = input()  # Message being sent
    if sending.lower() == 'q':  # Exit the program
        break
    date_now = datetime.now().strftime('%m-%d-%Y %H:%M:%S')  # Find current date/time
    to_send = f"{uCOLOR}[{date_now}] {name}: {sending}{Fore.RESET}"  # Structure message
    tcp.send(to_send.encode())  # Send Message

tcp.close()  # Close socket
