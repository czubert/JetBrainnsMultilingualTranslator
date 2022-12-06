class WordError(Exception):
    def __init__(self):
        self.message = "Wrong!"
        super().__init__(self.message)


def check_w_letter(word):
    if "w" in word:
        raise WordError
    return word
