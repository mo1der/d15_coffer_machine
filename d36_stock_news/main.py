import requests
import pandas


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_KEY = "IU5H8YNGMMM6M4EF"


NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={ALPHA_KEY}&slice=year1month1'
r = requests.get(url)
data = r.json()['Time Series (60min)']


new_data = [(key, value['1. open'], value['4. close']) for (key, value) in data.items()]  # ['a', 'b']
print(new_data)

new_data2 = pandas.DataFrame(data).transpose()
print(new_data2.info())
new_data3 = new_data2.drop(new_data2.columns[[1, 2, 4]], axis=1)
print(new_data3)

new_data3.reset_index(level=0, inplace=True)

new_data3.rename(columns={"index": "Data", "1. open": "Open", "4. close": "Close"}, inplace=True)
print(new_data3)

new_data3[['Date','Hour']] = new_data3.Data.str.split(' ',expand=True)
print(new_data3)

# Drop a row by condition
new_data3 = new_data3[new_data3.Hour.isin(["20:00:00", "05:00:00"])]
new_data3['Open'] = new_data3['Open'].astype(float)
new_data3['Close'] = new_data3['Close'].astype(float)
print(new_data3.dtypes)

new_data3['Difference'] = new_data3.apply(lambda row: ((row.Close-row.Open)/row.Close), axis=1)

new_data3 = new_data3.sort_values(by=['Data'], ascending=True)
print(new_data3)

new_data3.change.shift(1) - new_data3.change

#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

