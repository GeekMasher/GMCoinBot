
import json
import logging
from datetime import datetime

import ccxt
import gmutils


# GMUtils will load this from configuration files
class Config(gmutils.Config):
    API_KEYS = {}

    DEFAULT_SYMBOL = 'BTC/USD'
    DEFAULT_TIMECACHE = 30  # in seconds

    USERS = {}

    exchange = ccxt.kraken()

    markets = exchange.load_markets()
    symbols = list(ccxt.Exchange.keysort(markets).items())

    price = {
        'BTC/USD': {
            'price': '100.00 (t)',
            'last_update': 0
        }
    }

    @classmethod
    def loadFile(cls, path_file):
        super(Config, cls).loadFile(path_file)

        for user, vals in Config.USERS.items():
            if isinstance(Config.USERS[user].get('exchange'), str):
                ex = Config.USERS[user].get('exchange').lower()
                Config.USERS[user]['exchange'] = getattr(ccxt, ex)()

    @staticmethod
    def getPrice(symbol='BTC/USD', exchange=None):
        if Config.isTesting():
            return '100.00 (T)'

        if exchange is None:
            exchange = ccxt.kraken()

        # if the symbol hasn't been used before:
        if Config.price.get(symbol) is None:
            Config.price[symbol] = {
                'price': 'N/A',
                'time': 0
            }

        price = Config.price.get(symbol)
        current_epoch = datetime.now().timestamp()
        diff = price.get('last_update', 0) + Config.DEFAULT_TIMECACHE
        
        if diff <= current_epoch:
            logging.debug('getPrice() :: fetching new price from exchange')

            new_price = exchange.fetch_ticker(
                symbol
            ).get('bid', 'N/A')

            Config.price[symbol] = {
                'price': new_price,
                'last_update': current_epoch
            }
        else:
            logging.debug('getPrice() :: cached copy used')

        return Config.price.get(symbol).get('price')

    @staticmethod
    def checkSymbol(sym):
        for wl_symbol, _ in Config.symbols:
            if wl_symbol == sym:
                return True
        return False

    @staticmethod
    def checkExchanges(exchange):
        return exchange in ccxt.exchanges

    @staticmethod
    def getChatSettings(chat):
        user = chat.title if chat.type == 'group' else chat.username
        
        if not Config.USERS.get(user):
            Config.USERS[user] = {
                'exchange': getattr(ccxt, 'kraken')(),
                'symbol': 'BTC/USD'
            }
        return Config.USERS.get(user)

    @staticmethod
    def updateChatSettings(user, exchange=None, symbol=None):

        if Config.USERS.get(user):
            if exchange is not None:
                Config.USERS[user]['exchange'] = getattr(
                    ccxt, exchange
                )()
            if symbol is not None:
                Config.USERS[user]['symbol'] = symbol
        
    @staticmethod
    def __export__():
        groups = {}
        for user, vals in Config.USERS.items():
            groups[user] = {
                'exchange': vals.get('exchange').name,
                'symbol': vals.get('symbol'),
            }

        ret_val = {
            'DEFAULT_SYMBOL': Config.DEFAULT_SYMBOL,
            'USERS': groups,
            'price': Config.price
        }
        return ret_val
