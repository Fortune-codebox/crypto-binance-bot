#!/usr/bin/env python

from sqlalchemy import create_engine
import pandas as pd
import datetime as dt
from binance.client import Client
import asyncio
from binance import AsyncClient, BinanceSocketManager
import json

from main import get_project_settings

import_filepath = "settings.json"
# nest_asyncio.apply()

project_settings = get_project_settings(import_filepath)

API_Key = project_settings['BinanceKeysSpot']['API_Key']
Secret_Key = project_settings['BinanceKeysSpot']['Secret_Key']

client = Client(API_Key, Secret_Key, testnet=True)

engine = create_engine(
    'sqlite:////CrytoDB.db')

# pd.read_sql('BTCUSDT', engine)
# import os
# if os.path.exists('CrytoDB.db'):
#     os.remove('CrytoDB.db')

# print('Database removed successfully!')

symbols = pd.read_sql(
    'SELECT name FROM sqlite_master WHERE type="table"', engine).name.to_list()


def qry(symbol, lookback: int):
    now = dt.datetime.now() + dt.timedelta(hours=4)
    before = now - dt.timedelta(minutes=lookback)
    qry_strng = f"""SELECT * FROM '{symbol}' WHERE TIME >= '{before}'"""
    return pd.read_sql(qry_strng, engine)


def writeToFile(msg):
    if type(msg) == dict:
        msg = json.dumps(msg, indent=2)

    with open('/Users/fortunecodebox/documents/Learning-Python/Bots/output.txt', 'a') as f:
        f.write(msg + '\n')


rets = []
for symbol in symbols:
    prices = qry(symbol, 3).Price
    # cumret means cummulative returns
    cumret = (prices.pct_change() + 1).prod() - 1
    rets.append(cumret)


top_coin = symbols[rets.index(max(rets))]

print('top_coin: ', top_coin)

investment_amt = 100


info = client.get_symbol_info(symbol=top_coin)

print('lll: ', [i for i in info['filters'] if i['filterType']
                == 'LOT_SIZE'][0]['minQty'])

Lotsize = float([i for i in info['filters'] if i['filterType']
                 == 'LOT_SIZE'][0]['minQty'])

price = float(client.get_symbol_ticker(symbol=top_coin)['price'])
arr = []
arr.append(investment_amt/price)
print('lotSize: ', Lotsize)

if 'e-' in str(Lotsize):
    ff = format(Lotsize, 'f')
    buy_quantity = round(investment_amt/price, len(ff.split('.')[1]))

else:
    buy_quantity = round(investment_amt/price, len(str(Lotsize).split('.')[1]))


free_usd = [i for i in client.get_account()['balances'] if i['asset']
            == 'USDT'][0]['free']

free_usd

if float(free_usd) > investment_amt:

    order = client.create_order(
        symbol=top_coin, side='BUY', type='MARKET', quantity=buy_quantity)

    writeToFile(order)
else:
    writeToFile('Order has not been executed, you are already invested!!!')
    quit()

buyprice = float(order['fills'][0]['price'])


def createframe(msg):
    df = pd.DataFrame([msg])
    df = df.loc[:, ['s', 'E', 'p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df


async def main(coin):

    # client = await AsyncClient.create(API_Key, Secret_Key, testnet=True)
    bsm = BinanceSocketManager(client)
    ms = bsm.trade_socket(coin)
    async with ms as tscm:
        while True:
            res = await tscm.recv()
            if res:
                print('res res: ', res)
                frame = createframe(res)
                if frame.Price[0] < buyprice * 0.97 or frame.Price[0] > 1.005 * buyprice:
                    order = client.create_order(symbol=coin,
                                                side='SELL',
                                                type='MARKET',
                                                quantity=buy_quantity
                                                )
                    writeToFile(order)
                    loop.stop()
            client.close_connection()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(top_coin))
