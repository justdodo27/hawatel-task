import requests
import json
import typing
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


class CurrencyFetch:
    """
    A class to represent a currency fetcher.

    ...

    Attributes
    ----------
    code : str
        currency code
    url : str
        url from which the data will be fetched
    headers : dict
        header for request fetch


    Methods
    -------
    _fetch():
        Fetchs the currency data from NBP API.
    """
    def __init__(self, *, code: str):
        """
        Constructs all the necessary atributes for the CurrencyFetch object.

        Parrameters
        ----------
            code : str
                currency code
        """
        self.code = code
        self.url = (
            f"http://api.nbp.pl/api/exchangerates/rates/a/{self.code}/"
        )
        self.headers = {"Accept": "application/json"}

    def _fetch(self) -> typing.Dict:
        """
        Fetchs the currency data from NBP API.

        Returns:
            data (dict): Dictionary data of the currency rate
        """
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            logging.info(f"Succesfully fetched exchange rate")
        else:
            logging.error(f"API response with {response.status_code}")
            return None
        data = json.loads(response.text)

        return data
