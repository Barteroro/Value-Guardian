import requests 
from bs4 import BeautifulSoup
import os


URL = "https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=ZLOTO"
selektor = "#quotes-profile-header-box > div.o-quotes-profile-header-box__top > div.o-quotes-profile-header-box__numbers > div.o-quotes-profile-header-box__data > div.o-quotes-profile-header-box__price > span"

HEADERS= {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(URL, headers = HEADERS)
soup = BeautifulSoup(response.text, "html.parser")
cena =soup.select_one(selektor)
if cena:
    cena_sama = cena.text.strip("USD")
    cena_sama = cena_sama.replace("\xa0", "")
    cena_sama = int(round(float((cena_sama.replace(" ", "")).replace(",", "."))))
    print("Bot odczytał cene: {}".format(cena_sama))
else:
    print("Bot nic nie zlalazł, gg")
if os.path.exists("dane.txt") and os.path.getsize("dane.txt") > 0:
    with open("dane.txt", "r") as Tr:
        odczyt = Tr.readlines()
        najstarsze = int(odczyt[0].strip())
        spadek = najstarsze * 0.8
        if cena_sama <= spadek:
            print("Cena spadłą, najnowsza {}, najstarsza {}".format(cena_sama, najstarsze))
        else:
            pass
else:
    print("To pierwsze uruchomienie")
with open("dane.txt", "a") as Ta:
    Ta.write("{}\n".format(cena_sama))
    

    