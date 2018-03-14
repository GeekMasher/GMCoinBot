
import ccxt


def getCurrent(exchange_name='kraken', symbol='ETH/USD'):

    exchange = ccxt.kraken()
    ticker = exchange.fetch_ticker(symbol)


def getExchangesSupported():
    ret_val = []
    for item in dir(ccxt):
        if item.startswith('_') or item == "Exchange":
            continue
        attr = getattr(ccxt, item)
        if inspect.isclass(attr) and issubclass(attr, ccxt.Exchange):
            ret_val.append(attr)
    return ret_val
