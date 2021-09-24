from typing import Iterable, Union
import math


class String:
    def __init__(self, content: Iterable[str], parse_alphabet: Union[Iterable, None] = None):
        if parse_alphabet is None:
            parse_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.content = content
        self.parse_alphabet = parse_alphabet

    def __str__(self):
        return ''.join(self.content)

    def __repr__(self):
        return '<object String>'

    def __iter__(self):
        return self.content

    def transtable(self, encode_alphabet):
        return {a: b for a, b in zip(self.parse_alphabet, encode_alphabet)}

    def translate(self, encode_alphabet):
        table = self.transtable(encode_alphabet)
        def content():
            for char in self.content:
                yield table.get(char, char)
        return String(content, self.parse_alphabet)

    def shift_translate(self, shift: int):
        if shift <= 0:
            shift += len(self.content)
        alphabet = self.parse_alphabet[shift:] + self.parse_alphabet[:shift]
        return self.translate(alphabet)

    def square_translate(self):
        if len(self.parse_alphabet) > 100:
            raise ValueError('Parse alphabet is too long')
        width = math.ceil(math.sqrt(len(self.parse_alphabet)))
        def encode_alphabet():
            for w in range(width):
                for h in range(width):
                    yield f'{w}{h}'
        return self.translate(encode_alphabet())
