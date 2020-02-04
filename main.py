import requests
import urllib3
import re
from bs4 import BeautifulSoup

#url = "https://br.investing.com/equities/petrobras-pn-news"
url = "https://br.investing.com//news/stock-market-news/"
cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}


# Invocando o metodo

resposta = requests.get(url, headers=cabecalho)

html = resposta.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')

crawling = soup.find_all('a')


for link in crawling:
    #print (link.get('href'))
    print(link.get_text())