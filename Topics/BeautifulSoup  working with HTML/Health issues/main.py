import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()
# url = "http://web.archive.org/web/20201201053628/https://www.who.int/health-topics"

req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

paragraphs = soup.find_all('a')

result = []

for i in paragraphs:
    p = i.text
    if len(p) > 1 and p.startswith(letter):
        if 'topics' in i.get('href') or 'entity' in i.get('href'):
            result.append(p)
print(result)
