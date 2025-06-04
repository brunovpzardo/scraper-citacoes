# Esse programa é um exemplo de como criar um scraper de uma página simples da internet ee retirar informaçoes especificas.
# Foram utilizadas as bibliotecas requests e BeautifulSoup


import requests
from bs4 import BeautifulSoup

# Site utilizado para retirar as informações

url = 'https://quotes.toscrape.com/'
site = requests.get(url)

# Extração da informação

soup = BeautifulSoup(site.text, 'html.parser')

# Procura as ocorrências da tag span e da tag small onde possuam a classe CSS de text e de autor respectivamente

Citacoes = soup.find_all('span', class_='text')
Autores = soup.find_all('small', class_='author')

# Imprime as Citações encontradas no formato de Citação - Autor

for Citacao, Autor in zip(Citacoes,Autores):
    print(f'{Citacao.text} - {Autor.text}')
