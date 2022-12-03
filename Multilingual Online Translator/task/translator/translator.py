import requests
from bs4 import BeautifulSoup


class Translator:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.__languages = {0: 'All', 1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French', 6: 'Hebrew',
                            7: 'Japanese', 8: 'Dutch', 9: 'Polish', 10: 'Portuguese',
                            11: 'Romanian', 12: 'Russian', 13: 'Turkish'}
        self.source_lang = ''
        self.direction_lang = ''
        self.word = ''

    def main(self):
        transl.greet()
        soup = transl.get_web_content()
        if soup:
            transl.get_translations(soup)
            transl.get_examples(soup)
        else:
            print('Please try again')

    def greet(self):
        welcome_msg = 'Hello, welcome to the translator. Translator supports:'
        print(welcome_msg)
        for i, el in self.__languages.items():
            print(f"{i}. {el}")

        print("Type the number of your language: ")
        user_lang = int(input())
        self.source_lang = self.__languages[user_lang]

        print('Type the number of language you want to translate to:')
        transl_lang = int(input())
        self.direction_lang = self.__languages[transl_lang]

        print('Type the word you want to translate:')
        self.word = input()
        # self.word = 'dom'

        print(f'You chose "{self.direction_lang}" as the language to translate "{self.word}" to.')

    def get_web_content(self):
        url_core = "https://context.reverso.net/translation"
        url = f"{url_core}/{self.source_lang.lower()}-{self.direction_lang.lower()}/{self.word}"

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
        print(f'{self.direction_lang} Translations:')

        if len(translations) == 0:
            print("We are sorry, we do not support this pair of languagues")
        else:
            print(*translations, sep='\n', end='\n\n')

    def get_examples(self, soup):
        lines = soup.find_all('div', {'class': ['src ltr', 'trg ltr']})
        print(f'{self.direction_lang} Examples:')

        for i, line in enumerate(lines):
            if i % 2 == 0 and i != 0:
                print()
            tmp_example = (" ".join(line.text.split()))
            if len(tmp_example) == 0:
                continue
            else:
                print(tmp_example)


transl = Translator()
transl.main()
