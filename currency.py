import requests
import json
import typing

class APIResponse404(Exception):
    """Raised when API responds with 404"""
    pass

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
    logger : Logger object
        logger object for debuging


    Methods
    -------
    _fetch():
        Fetchs the currency data from NBP API.
    """
    def __init__(self, *, code: str, logger):
        """
        Constructs all the necessary atributes for the CurrencyFetch object.

        Parrameters
        ----------
            code : str
                currency code
            logger : Logger object
                logger object for debuging
        """
        self.code = code
        self.url = (
            f"http://api.nbp.pl/apj/exchangerates/rates/a/{self.code}/"
        )
        self.headers = {"Accept": "application/json"}
        self.logger = logger

    def _fetch(self) -> typing.Dict:
        """
        Fetchs the currency data from NBP API.

        Returns:
            data (dict): Dictionary data of the currency rate
        """

        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.logger.info(f"Succesfully fetched exchange rate")
            elif response.status_code == 404:
                raise APIResponse404
            data = json.loads(response.text)
            return data
        except APIResponse404:
            self.logger.error("API response with HTTP 404 Not Found")
            raise SystemExit("API response with HTTP 404 Not Found")

