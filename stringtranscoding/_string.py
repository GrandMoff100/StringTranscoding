from .base import BaseString


class _String(BaseString):
    def __eq__(self, other):
        self._type_check(other)
        return self.parse_alphabet == other.parse_alphabet and \
            self.content == other.content and \
            self.sep == other.sep

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        self._type_check(other)
        if self.parse_alphabet == other.parse_alphabet and self.

    def _type_check_(self, other):
        if isinstance(other, self.__class__):
            raise ValueError('{} is not of type {}'.format(other, self.__class__))
