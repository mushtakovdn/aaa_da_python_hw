import keyword
from typing import Any, Union
import json


class Advert:

    def __init__(self, mapping: dict):
        self._parse_dict(mapping)

    # def __setattr__(self, name: str, value: Any):
    #     if name == 'price':
    #         pass
    #     if keyword.iskeyword(name):
    #         name += '_'
    #     self.__dict__[name] = value

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
                self.__setattr__(attr, value)
            else:
                # self.price = value
                pass



if __name__ == '__main__':
    dog_str = """{
        "title": "Вельш-корги",
        "price2": 1000,
        "class": "dogs"
    }"""
    dog = json.loads(dog_str)
    dog_ad = Advert(dog)
    dog_ad.price = -500
    print(dog_ad.__dict__)
    print(dog_ad.price)

  