# import pybit
# import requests
# from pybit import inverse_perpetual
import ccxt

def get_currencies_bybit():
    exchange = ccxt.bybit()
    tickers = sorted(list(exchange.fetch_tickers().items()), key=lambda x: x[1]['high'] if x[0].endswith('USDT') else 0,
                     reverse=True)
    data = [{'name': ticker[0][:-10], 'price': ticker[1]['high']} for ticker in tickers[:10]]
    return data


def get_currencies_binance():
    exchange = ccxt.binance()
    markets = exchange.load_markets()
    len_ = 0
    data = []
    tickers = exchange.fetch_tickers()
    for market in markets:
        if market[-4:] == 'USDT' and len_ < 10:
            if tickers[market]['high'] > 1:
                len_ += 1
                data.append({'name': market[:-5], 'price': tickers[market]['high']})

    return data


def get_all_exchanges():
    data_binance = get_currencies_binance()
    data_bybit = get_currencies_bybit()
    data = {"Binance": data_binance, "Bybit": data_bybit}
    return data

def get_exchange_by_name(name):
    if name in exchange_getters:
        return exchange_getters.get(name)()

exchange_getters = {
    'binance': get_currencies_binance,
    'bybit': get_currencies_bybit,
}
