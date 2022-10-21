from typing import Union
import requests
from commands import Command
from bankrupt import Bankrupt
import pandas as pd

class SoviaClient():
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    _request = requests.Session()
    _base_endpoint = ""

    def set_auth_headers(self):
        headers = {
            "X-Api-Key": self.api_key,
            "Accept": "application/json"
        }
        return self._request.headers.update(headers)

    def get(self, command: Command, *args: Union[object, Command]) -> Union[pd.DataFrame, list, tuple]:

        if command == Command.BANKRUPT and len(args) > 0:
            return Bankrupt(args=args)


sovia = SoviaClient(api_key="")

