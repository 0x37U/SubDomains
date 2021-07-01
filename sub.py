from requests import get
from colorama import Fore,Back
from colorama import init
import os
init(autoreset=True)

os.system("cls")

print("""
 ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗
██╔═████╗╚██╗██╔╝╚════██╗╚════██║██║   ██║
██║██╔██║ ╚███╔╝  █████╔╝    ██╔╝██║   ██║
████╔╝██║ ██╔██╗  ╚═══██╗   ██╔╝ ██║   ██║
╚██████╔╝██╔╝ ██╗██████╔╝   ██║  ╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═════╝ 
        Github : github.com/0x37U
""")

os.system("title [-] 0x37U SubDomain Finder v1 [-]")

Link = input(Fore.RED+"0x37U@Domain"+Fore.WHITE+":"+Fore.BLUE+"~"+Fore.WHITE+"#"" ").strip()

if "https://" or "http://" or "www." in Link:
	Link = Link.replace("https://","").replace("http://","").replace("www.","")

def subs(domain):

    url = f"https://sonar.omnisint.io/subdomains/{domain}"
    Data = get(url,timeout=5).json()

    if "null" in Data:

        print("Domain is Down !!")

    else:
        f = open(f"{Link}.txt","a")
        for i in Data:
            print(Fore.LIGHTGREEN_EX+i)
            f.write(i+"\n")
    
        print(Back.GREEN+f"<========= Check \"{domain}.txt\" File. =========>")
subs(Link)
