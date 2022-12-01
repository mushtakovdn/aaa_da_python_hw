import keyword
from typing import Union
import json


class Advert:

    def __init__(self, mapping: dict):
        self._parse_dict(mapping)

    @property
    def price(self):
        print('CALLED GETTER')
        if '_price' in self.__dict__:
            return self._price
        else:
            return 0

    @price.setter
    def price(self, value: Union[float, int]):
        print('CALLED SETTER')
        if value >= 0:
            self._price = value
        else:
            self._price = 'ValueError: must be >= 0'

    def _parse_dict(self, mapping: dict):
        """
        Парсинг входного json
        """
        for attr, value in mapping.items():
            if isinstance(value, dict):
                value = Advert(value)
            if attr != 'price':
                if keyword.iskeyword(attr):
                    attr += '_'
                self.__dict__[attr] = value
            else:
                self.price = value


if __name__ == '__main__':
    dog_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    print(dog_ad.__dict__)
    dog_ad.price = -500
    print(dog_ad.__dict__)
    print(dog_ad.price)
    print("\033[1;32;40m Bright Green  \n")

  