import requests

from bs4 import BeautifulSoup

idx = int(input())
web = input()

req = requests.get(web)

soup = BeautifulSoup(req.content, 'html.parser')

head = soup.find_all('h2')

print(head[idx].text)
