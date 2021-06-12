
from requests import get
from colorama import Fore,Back
from colorama import init
import os
R=Fore.RED
P=Fore.GREEN
sd=Fore.LIGHTGREEN_EX
s=Fore.BLACK
y=Fore.LIGHTYELLOW_EX
u=Fore.LIGHTRED_EX
a=Fore.LIGHTCYAN_EX
asd=Fore.LIGHTMAGENTA_EX
init(autoreset=True)

os.system("clear")

print(f"""
 {a} SUB4ME ~ SubdomaiN ScaNNER coded by M!l3z {a}
     {asd}  Facebook : George Miller{asd} (Lufifer)
               {y} Fvck L0v3 {y}



        Github : github.com/mile403
""")


Link = input(Fore.RED+"M!L3z"+Fore.WHITE+":"+Fore.BLUE+"~"+Fore.WHITE+"#"" ").strip()

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
            f.write(i)
    
        print(Back.GREEN+f"<========= Check \"{domain}.txt\" File. =========>")
subs(Link)
