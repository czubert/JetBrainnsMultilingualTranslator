import requests
from bs4 import BeautifulSoup


class Translator:

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.url_core = "https://context.reverso.net/translation"
        self.__languages = {0: 'All', 1: 'Arabic', 2: 'German', 3: 'English', 4: 'Spanish', 5: 'French', 6: 'Hebrew',
                            7: 'Japanese', 8: 'Dutch', 9: 'Polish', 10: 'Portuguese',
                            11: 'Romanian', 12: 'Russian', 13: 'Turkish'}
        self.source_lang = ''
        self.direction_lang = ''
        self.word = ''

    def main(self):
        self.greet()
        self.get_source_lang()
        transl_lang_nr = self.get_transl_lang()
        self.get_word_to_translate()

        if transl_lang_nr > 0:
            self.direction_lang = self.__languages[transl_lang_nr]
            soup = transl.get_web_content(self.direction_lang)
            if soup:
                self.get_translations(soup)
                self.get_examples(soup)
            else:
                print('Please try again')
        else:
            for lang in self.__languages.values():
                if lang == 'All':
                    continue
                soup = transl.get_web_content(lang)
                if soup:
                    self.get_translations(soup, lang, multi=True)
                    self.get_examples(soup, lang, multi=True)
        with open(f'{self.word}.txt', 'r', encoding='utf-8') as f:
            for el in f.readlines():
                print(el, end='')

    def greet(self):
        welcome_msg = 'Hello, welcome to the translator. Translator supports:'
        print(welcome_msg)
        for i, el in self.__languages.items():
            print(f"{i}. {el}")

    def get_source_lang(self):
        print("Type the number of your language: ")
        user_lang = int(input())
        self.source_lang = self.__languages[user_lang]

    def get_transl_lang(self):
        print("Type the number of a language you want to translate to or '0' to translate to all languages:")
        transl_lang_nr = int(input())
        return transl_lang_nr

    def get_word_to_translate(self):
        print('Type the word you want to translate:')
        self.word = input()

    def get_web_content(self, direction_lang):
        url = f"{self.url_core}/{self.source_lang.lower()}-{direction_lang.lower()}/{self.word}"
        page = requests.get(url, headers=self.headers)
        conn_status = page.status_code

        if conn_status == 200:
            return BeautifulSoup(page.content, 'html.parser')
        elif conn_status == 404:
            print("Page doesn't exist")
            return False
        else:
            print('Unexpected error has occurred')
            return False

    def get_translations(self, soup, language=None, multi=False):
        paragraphs = soup.find_all('span', {'class': 'display-term'})
        translations = []

        for i in paragraphs:
            translations.append(i.text)

        if len(translations) == 0:
            pass
        elif multi:
            self.add_to_file(f'{language} Translations:')
            self.add_to_file(translations[0] + '\n')
        else:
            self.add_to_file(f'{self.direction_lang} Translations:')
            for el in translations:
                self.add_to_file(el)

    def get_examples(self, soup, language=None, multi=False):
        lines = soup.find_all('div', {'class': ['src ltr', 'trg ltr']})

        if not multi:
            self.add_to_file("\n" + f'{self.direction_lang} Examples:')

            for i, line in enumerate(lines):
                if i % 2 == 0 and i != 0:
                    # print()
                    self.add_to_file('\n')
                tmp_example = (" ".join(line.text.split()))
                if len(tmp_example) == 0:
                    continue
                else:
                    # print(tmp_example)
                    self.add_to_file(tmp_example)

        elif multi:
            if language == self.source_lang:
                return
            self.add_to_file(f'{language} Example:')
            for i, line in enumerate(lines):
                if i < 2:
                    tmp_example = (" ".join(line.text.split()))
                    self.add_to_file(tmp_example)
            self.add_to_file('\n')
        else:
            print('Something went wrong with get_examples')

    def add_to_file(self, content):
        with open(f'{self.word}.txt', 'a+', encoding='utf-8') as f:
            f.write(content + '\n')


transl = Translator()
transl.main()
