import requests
import json
import typing
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class CurrencyFetch:
    def __init__(self, *, code: str):
        self.code = code
        self.table = 'a'
        self.url = f'http://api.nbp.pl/api/exchangerates/rates/{self.table}/{self.code}/'
        self.headers = {'Accept': 'application/json'}

    def _fetch(self) -> typing.Dict:
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            logging.info(f'Succesfully fetched exchange rate')
        else:
            logging.error(f'API response with {response.status_code}')
            return None
        data = json.loads(response.text)

        return data