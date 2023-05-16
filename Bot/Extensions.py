import requests
import json
from Config import keys

class ConvertionException(Exception):
    pass
class CryptoConverte:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно конвертировать одинаковые валюты {base}.')
        elif amount <= '0':
            raise ConvertionException (f'Количество валюты должно быть больше нуля')
        try:
            quote_tickir = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_tickir = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количестов {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tickir}&tsyms={base_tickir}')

        total_base = (json.loads(r.content)[keys[base]])*amount


        return total_base