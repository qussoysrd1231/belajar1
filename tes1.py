import requests
from bs4 import BeautifulSoup
from time import sleep


url = "https://freebitcoincash.cryptoplanets.org/DJSNChdiej73dosN8S7KcyJltcfaucet/moreapps.php"

UA = {
  "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36"
}

data = {
 "PHPSESSI": "Demg823ito7g3q3cp02dgtonsc4"
}


c = requests.Session()


def login():
    r = c.post(url, cookies=data, 
headers=UA)
    soup = BeautifulSoup(r.content,"html.parser")
    print (soup)
login()
