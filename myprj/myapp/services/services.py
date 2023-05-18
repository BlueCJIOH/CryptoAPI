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
    if name in exchange_getters_currencies:
        return exchange_getters_currencies.get(name, 'None')()
    else:
        return 'Not found'


def get_binance_by_currency(name):
    exchange = ccxt.binance()
    try:
        ticker = exchange.fetch_tickers([f'{name}/USDT', ])
        return {
            'name': name,
            'price': ticker.get(f'{name}/USDT')['high'],
        }
    except ccxt.errors.BadSymbol:
        return {
            'name': 'Not found',
            'price': 'Not found',
        }


def get_bybit_by_currency(name):
    exchange = ccxt.bybit()
    try:
        ticker = exchange.fetch_tickers([f'{name}/USDT:USDT', ])
        return {
            'name': name,
            'price': ticker.get(f'{name}/USDT:USDT')['high'],
        }
    except ccxt.errors.BadSymbol:
        return {
            'name': 'Not found',
            'price': 'Not found',
        }


def get_exchange_by_currency(name, cname):
    if name in exchange_getters_currency:
        return exchange_getters_currency.get(name)(cname)
    else:
        return 'Not found'


def get_binance_currencies_names():
    return [el[0] for el in
            filter(lambda x: x[1] == 'USDT', map(lambda x: x.split('/'), ccxt.binance().load_markets().keys()))][:20]


def get_bybit_currencies_names():
    return [el[0] for el in
            filter(lambda x: x[1][:4] == 'USDT' and len(x[0]) < 4,
                   map(lambda x: x.split('/'), ccxt.bybit().load_markets().keys()))]


def get_names_from_exchange(name):
    if name in exchange_getters_currencies_names:
        return exchange_getters_currencies_names.get(name)()
    else:
        return 'Not found'


def get_names_from_exchanges():
    return [{exchange[0].capitalize(): exchange[1]()} for exchange in exchange_getters_currencies_names.items()]


exchange_getters_currencies = {
    'binance': get_currencies_binance,
    'bybit': get_currencies_bybit,
}
exchange_getters_currency = {
    'binance': get_binance_by_currency,
    'bybit': get_bybit_by_currency,
}
exchange_getters_currencies_names = {
    'binance': get_binance_currencies_names,
    'bybit': get_bybit_currencies_names,
}
