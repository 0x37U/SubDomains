from requests import get

import os

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

Link = input("0x37U@Domain:~# ").strip()

def subs(domain):

    url = f"http://jamet1337.ml/api/same-domain.php?url={domain}"
    Data = get(url,timeout=5)
    Json = Data.json()
    domains = Json['hasil'].split("\r")
    if "Gagal Memuat Data" in domains:

        print("Domain is Down !!")
    else:
        f = open(f"{Link}.txt","a")
        for i in domains:
            print(i)
            f.write(i)
    
        print("<========= Check \"Subs.txt\" File. =========>")
subs(Link)
