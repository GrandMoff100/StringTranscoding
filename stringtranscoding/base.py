from typing import Iterable, Union


class BaseString:
    def __init__(self, content: Iterable[str], parse_alphabet: Union[Iterable, None] = None, sep=None):
        if sep is None:
            sep = ""
        if parse_alphabet is None:
            parse_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.content = content
        self.parse_alphabet = parse_alphabet

    def __str__(self):
        return self.sep.join(self.content)

    def __repr__(self):
        return "<translatable String>"

    def __iter__(self):
        return self.content

    def transtable(self, encode_alphabet):
        return {a: b for a, b in zip(self.parse_alphabet, encode_alphabet)}

    def translate(self, encode_alphabet, *args, **kwargs):
        table = self.transtable(encode_alphabet)
        def content():
            for char in self.content:
                yield table.get(char, char)
        return self.__class__(content, self.parse_alphabet, *args, **kwargs)

    def from_string(self, string):
        return self.__class__(string.split(self.sep), self.parse_alphabet, self.sep)
