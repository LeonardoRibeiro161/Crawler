import requests
import urllib3
import re
import argparse
import sys
from bs4 import BeautifulSoup

def buscar_conteudo(url):
    #url = "https://br.investing.com/equities/petrobras-pn-news"
    # url = "https://br.investing.com/news/stock-market-news/"
    cabecalho = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    resposta = requests.get(url, headers=cabecalho)

    html = resposta.text

    soup = BeautifulSoup(html, 'html.parser')

    crawling = soup.find_all(class_="textDiv")

    for link in crawling:
        print(link.get_text())

try:
    parse = argparse.ArgumentParser(description="Obtendo noticias do Investing")
    parse.add_argument("-u", "--url", help="Informe a url")
    args = parse.parse_args()
    url = sys.argv[2]
    buscar_conteudo(url)
except:
    print("Houve um erro na passagem de parametro, utilize -u url")

