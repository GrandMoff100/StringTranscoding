import math
from ._string import _String


class String(_String):
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
        return self.translate(encode_alphabet(), sep=' ')
