from typing import List
import re


class RowToVector:
    def __init__(self, row: List[str]):
        self.row: List[str] = [word for line in row for word in line.split()]
        self.funcs: List = []
        self.vector = []
        self.__init_funcs()
        for func in self.funcs:
            self.vector.append(func())

    def __init_funcs(self):
        self.funcs.append(self.number_of_words)
        self.funcs.append(self.percentage_of_non_letters)
        self.funcs.append(self.has_link)
        self.funcs.append(self.percentage_of_capital_letters)

    def number_of_words(self) -> int:
        return len(self.row)

    def percentage_of_non_letters(self) -> float:
        non_letter_sign = 0
        for word in self.row:
            for index, letter in enumerate(word):
                if ord(word[index]) > 122 or ord(word[index]) < 65:
                    non_letter_sign += 1
        return non_letter_sign / self.number_of_words()

    def has_link(self) -> bool:
        return re.search(
            "((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", ''.join(self.row)) is None

    def percentage_of_capital_letters(self) -> float:
        non_letter_sign = 0
        for word in self.row:
            for index, letter in enumerate(word):
                if ord(word[index]) > 64 or ord(word[index]) < 91:
                    non_letter_sign += 1
        return non_letter_sign / self.number_of_words()
