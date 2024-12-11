import configparser
import requests
import pandas as pd
from datetime import datetime
import ast

# file to save data
FILE_NAME = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + "_balance_history.csv"

# Read the config file
config = configparser.ConfigParser()
config.read("../alpaca.ini")
api = config['ALPACA']['api']
secret = config['ALPACA']['secret']

url = "https://paper-api.alpaca.markets/v2/account/portfolio/history?intraday_reporting=market_hours&pnl_reset=per_day"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": api,
    "APCA-API-SECRET-KEY": secret
}

response = requests.get(url, headers=headers)

bal_history = pd.DataFrame(ast.literal_eval(response.text))
bal_history['timestamp'] = pd.to_datetime(bal_history['timestamp'],unit='s')

bal_history.to_csv(FILE_NAME,index=False)
