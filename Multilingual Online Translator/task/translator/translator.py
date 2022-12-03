import requests
from bs4 import BeautifulSoup
import re


class Translator:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.direction = ''
        self.word = ''
        self.lang = ''

    def main(self):
        transl.greet()
        transl.check_transl_direction()
        soup = transl.get_web_content()
        if soup:
            transl.get_translations(soup)
            transl.get_examples(soup)
        else:
            print('Please try again')

    def greet(self):
        welcome_msg = 'Type "en" if you want to translate from French into English, ' \
                      'or "fr" if you want to translate from English into French:'

        print(welcome_msg)
        # self.direction = input()
        self.direction = 'fr'

        print('Type the word you want to translate:')
        # self.word = input()
        self.word = 'hello'

        print(f'You chose "{self.direction}" as the language to translate "{self.word}" to.')

    def check_transl_direction(self):
        if self.direction == 'en':
            self.direction = 'french-english'
            self.lang = 'English'
        else:
            self.direction = 'english-french'
            self.lang = 'French'

    def get_web_content(self):

        url = f"https://context.reverso.net/translation/{self.direction}/{self.word}"

        page = requests.get(url, headers=self.headers)
        conn_status = page.status_code

        if conn_status == 200:
            print('200 OK')
            return BeautifulSoup(page.content, 'html.parser')
        elif conn_status == 404:
            print("Page doesn't exist")
            return False
        else:
            print('Unexpected error has occureds')
            return False

    def get_translations(self, soup):
        paragraphs = soup.find_all('span', {'class': 'display-term'})
        translations = []

        for i in paragraphs:
            translations.append(i.text)
        print()
        print(f'{self.lang} Translations:')
        print(*translations, sep='\n', end='\n\n')

    def get_examples(self, soup):
        lines = soup.find_all('div', {'class': ['src ltr', 'trg ltr']})
        print(f'{self.lang} Examples:')

        for i, line in enumerate(lines):
            if i % 2 == 0 and i != 0:
                print()
            tmp_example = (" ".join(line.text.split()))
            print(tmp_example)


transl = Translator()
transl.main()
