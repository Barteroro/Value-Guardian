import requests 
from bs4 import BeautifulSoup
import os


URL = "https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ZLOTO"
DISCORD_WEEBHOOK = "https://discord.com/api/webhooks/1546203996367360210/DPQ5sema5EU6HScUC7DxzxOVbEOOzv9VFHg7wNcvKNOK1GHGigFqAOlz1J1u5l_7Ep-A"
HEADERS= {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

selektor = "#quotes-profile-header-box > div.o-quotes-profile-header-box__top > div.o-quotes-profile-header-box__numbers > div.o-quotes-profile-header-box__data > div.o-quotes-profile-header-box__price > span"


response = requests.get(URL, headers = HEADERS)
soup = BeautifulSoup(response.text, "html.parser")
cena =soup.select_one(selektor)

if cena:
    cena_nowa = cena.text.replace("USD", "")
    cena_nowa = cena_nowa.replace("\xa0", "")
    cena_nowa = int(round(float((cena_nowa.replace(" ", "")).replace(",", "."))))
    print("Bot odczytał cene: {}".format(cena_nowa))
else:
    print("Bot nic nie zlalazł, gg")

linie = []
if os.path.exists("dane.txt") and os.path.getsize("dane.txt") > 0:
    with open("dane.txt", "r") as Tr:
        linie = [linia.strip() for linia in Tr.readlines() if linia.strip()]
if linie:
        najstarsze = int(linie[0])
        spadek = najstarsze * 0.8
        
        if cena_nowa <= spadek:
            discord = {"content": "Cena spadła, najnowsza {}, najstarsza {}".format(cena_nowa, najstarsze)}
            try:
                requests.post(DISCORD_WEEBHOOK, json = discord)
                print("Wysłało powiadomienie")
            except Exception as e:
                print("NIE wysłało powiadomienia {}".format(e))


        else:
            pass

else:
    pass
linie.append(cena_nowa)
if len(linie) > 60:
    linie.pop(0)
with open("dane.txt", "w") as Ta:
    for i in linie:
        Ta.write("{}\n".format(i))
    

    