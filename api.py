from typing import List, Optional
from datetime import datetime

import requests
from pprint import pprint


class BT_API:

    COIN_NAME = {
        'eth_usdt': 'Ethereum',
        'btc_usdt': 'Bitcoin',
        'ltc_usdt': 'Litecoin',
        'pzm_usdt': 'Prizm',
        'trx_usdt': 'Tron',
        'bnb_usdt': 'Binance coin',
        'del_usdt': 'Decimal',
    }

    def __init__(self) -> None:

        # urls
        self.BASE_URI = "https://bit.team/trade/api"
        self.GET_PAIRS = self.BASE_URI + "/pairs"

    def get_pairs(self):
        pairs = requests.get(
            self.GET_PAIRS
        ).json()

        result = {}
        for pair in pairs['result']['pairs']:
            if "usdt" in pair['name']:
                coin_name = self.COIN_NAME[pair['name']]
                result[coin_name] = {
                    'code': int(pair['id']),
                    'name': self.COIN_NAME[pair['name']],
                    'price': float(pair['lastPrice']),
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'nominal': 1,
                }

        return result

    def get_prices(self, token_list: list) -> Optional[list]:
        result = []
        pairs = self.get_pairs()

        for token in token_list:
            if not token in list(self.COIN_NAME.values()):
                result.append({
                    'code': None,
                    'name': token,
                    'price': None,
                    'time': None,
                    'nominal': None,
                })
                continue
            result.append(pairs[token])

        return result
