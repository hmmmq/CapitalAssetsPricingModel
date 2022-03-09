import requests
import time

stat_time = "2013-1-1"
ending_time = "2016-1-1"
start_array = time.strptime(stat_time, "%Y-%m-%d")
ending_array = time.strptime(ending_time, "%Y-%m-%d")
start_stamp = int(time.mktime(start_array))
ending_stamp = int(time.mktime(ending_array))
stock_codes = ["FB", "PSY"]
period1 = start_stamp
period2 = ending_stamp
for stock_code in stock_codes:
    url = """https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true""".format(
        stock_code, period1, period2)
    response = requests.get(url=url)
    filename = stock_code + ".csv"
    print(filename + " downloading")
    with open(filename, "wb") as f:
        f.write(response.content)
