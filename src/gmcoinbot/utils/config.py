
import ccxt
import gmutils

# GMUtils will load this from configuration files
class Config(gmutils.Config):
    API_KEYS = {}

    DEFAULT_SYMBOL = 'BTC/USD'

    TELEGRAM_USERS = {}

    exchange = ccxt.kraken()

    markets = exchange.load_markets()
    symbols = list(ccxt.Exchange.keysort(markets).items())

    price = {
        'BTC/USD': '100.00 (t)'
    }

    @classmethod
    def load(cls):
        super(Config, cls).load()

        for user, vals in Config.TELEGRAM_USERS.items():
            ex = Config.TELEGRAM_USERS[user].get('exchange').lower()
            Config.TELEGRAM_USERS[user]['exchange'] = getattr(ccxt, ex)()
    
    @staticmethod
    def getPrice(symbol='BTC/USD', exchange=None):
        if Config.isTesting():
            return '100.00 (T)'

        if exchange is None:
            exchange = ccxt.kraken()

        Config.price[symbol] = exchange.fetch_ticker(
            symbol
        ).get('bid', 'N/A')

        return Config.price.get(symbol)

    @staticmethod
    def checkSymbol(sym):
        for wl_symbol, _ in Config.symbols:
            if wl_symbol == sym:
                return True
        return False

    @staticmethod
    def checkExchanges(exchange):
        return exchange in dir(ccxt)

    @staticmethod
    def getChatSettings(chat):
        user = chat.title if chat.type == 'group' else chat.username
        
        if not Config.TELEGRAM_USERS.get(user):
            Config.TELEGRAM_USERS[user] = {
                'exchange': getattr(ccxt, 'kraken')(),
                'symbol': 'BTC/USD'
            }
        return Config.TELEGRAM_USERS.get(user)

    @staticmethod
    def updateChatSettings(chat, exchange=None, symbol=None):
        user = chat.title if chat.type == 'group' else chat.username

        if Config.TELEGRAM_USERS.get(user):
            if exchange is not None:
                Config.TELEGRAM_USERS[user]['exchange'] = getattr(
                    ccxt, exchange
                )()
            if symbol is not None:
                Config.TELEGRAM_USERS[user]['symbol'] = symbol
        
    @staticmethod
    def __export__():
        groups = {}
        for user, vals in Config.TELEGRAM_USERS.items():
            groups[user] = {
                'exchange': vals.get('exchange').name,
                'symbol': vals.get('symbol'),
            }

        ret_val = {
            'API_KEYS': Config.API_KEYS,
            'DEFAULT_SYMBOL': Config.DEFAULT_SYMBOL,
            'TELEGRAM_USERS': groups,
            'price': Config.price
        }
        return ret_val
