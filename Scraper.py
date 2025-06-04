# Esse programa é um exemplo de como criar um scraper de uma página da para 


import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
site = requests.get(url)

soup = BeautifulSoup(site.text, 'html.parser')

Citacoes = soup.find_all('span', class_='text')
Autores = soup.find_all('small', class_='author')

for Citacao, Autor in zip(Citacoes,Autores):
    print(f'{Citacao.text} - {Autor.text}')
