from sqlalchemy import create_engine
import pandas as pd
from binance.client import Client
import asyncio
from binance import AsyncClient, BinanceSocketManager
# import nest_asyncio
from main import get_project_settings

import_filepath = "settings.json"
# nest_asyncio.apply()

project_settings = get_project_settings(import_filepath)

API_Key = project_settings['BinanceKeysSpot']['API_Key']
Secret_Key = project_settings['BinanceKeysSpot']['Secret_Key']

client = Client(API_Key, Secret_Key, testnet=True)

engine = create_engine('sqlite:///CrytoDB.db')


info = client.get_exchange_info()

symbols = [x['symbol'] for x in info['symbols']]

excludes = ['UP', 'DOWN', 'BEAR', 'BULL']

non_lev = [symbol for symbol in symbols if all(
    exclude not in symbol for exclude in excludes)]

relevant = [symbol for symbol in non_lev if symbol.endswith('USDT')]

multi = [i.lower() + '@trade' for i in relevant]


def createframe(msg):
    df = pd.DataFrame([msg['data']])
    df = df.loc[:, ['s', 'E', 'p']]
    df.columns = ['symbol', 'Time', 'Price']
    df.Price = df.Price.astype(float)
    df.Time = pd.to_datetime(df.Time, unit='ms')
    return df


async def main():
    client = await AsyncClient.create(API_Key, Secret_Key, testnet=True)
    bsm = BinanceSocketManager(client)
    ms = bsm.multiplex_socket(multi)

    async with ms as tscm:
        while True:
            res = await tscm.recv()
            if res:
                frame = createframe(res)
                frame.to_sql(frame.symbol[0], engine,
                             if_exists='append', index=False)

    await client.close_connection()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
