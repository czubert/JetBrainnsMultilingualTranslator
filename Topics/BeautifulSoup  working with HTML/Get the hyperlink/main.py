import requests

from bs4 import BeautifulSoup

act = int(input()) - 1
url = input()

print(BeautifulSoup(requests.get(url).content, 'html.parser').find_all('a')[act].get('href'))
