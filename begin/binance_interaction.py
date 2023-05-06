from binance.client import Client


# Function to query Binance and retrieve status
def query_binance_status():
    # Query for system status
    status = Client().get_system_status()
    print('status: ', status)
    if status['status'] == 0:
        return True
    else:
        raise ConnectionError

# Function to query Binance account


def query_account(api_key, api_secret):
    return Client(api_key, api_secret, testnet=True).futures_account()
