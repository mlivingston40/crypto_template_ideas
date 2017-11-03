import datetime
import pandas as pd
import requests

class Prices:
    def __init__(self, coin):

        self.coin = coin

        self.today_data = pd.DataFrame(requests.get("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_{}&start={}&period=300".format(self.coin,
            int(datetime.date.today().strftime("%s")))).json())

    # data from poloniex api , 5 minute candles
    def last_price(self):

        return self.today_data.weightedAverage.tail(1).item()

    def first_price(self):

        return self.today_data.weightedAverage.head(1).item()

    def widget_graph (self):

        output = []
        for a, b in zip(self.today_data.date, self.today_data.weightedAverage):
            output.append([a*1000, b])

        return output

