import requests
import datetime as dt

import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_KEY = "IU5H8YNGMMM6M4EF"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "4848a8fb6df64f3b9b29bcf9831c0dd1"


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
now = dt.date.today()

yesterday = dt.datetime.today() - dt.timedelta(days=1)
two_days_before = dt.datetime.today() - dt.timedelta(days=2)


url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK_NAME}&interval=60min&apikey={ALPHA_KEY}'
r = requests.get(url)
data = r.json()["Time Series (60min)"]
# print(data)
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

price_closing_yesterday = float(r.json()["Time Series (60min)"][f"{yesterday.date()} 20:00:00"]["4. close"])
# print(price_closing_yesterday)

#TODO 2. - Get the day before yesterday's closing stock price
price_closing_two_day_before = float(r.json()["Time Series (60min)"][f"{two_days_before.date()} 20:00:00"]["4. close"])
# print(price_closing_two_day_before)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(price_closing_yesterday - price_closing_two_day_before)
# print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

perc_difference = difference / price_closing_two_day_before
# print(perc_difference)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if perc_difference > 0.01:
    print("GET NEWS")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

url2 = f'https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2022-12-16&sortBy=popularity&apiKey={NEWS_KEY}'
r2 = requests.get(url2)
data2 = r2.json()["articles"]

print(data2)





#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
data3 = r2.json()["articles"][1:2]

print(data3)



    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

articles = [(news["title"], news["description"]) for news in data3]

for a in articles:
    print(f"{a[0]} oraz artykół\n{a[1]}\n")


#TODO 9. - Send each article as a separate message via Twilio.

    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client("AC157dea973ca8013c9620994a0fcbd646", "af4d9fa1a876bb0002a38c1bd8335c48")
    message = client.messages \
        .create(
        body=f"Headline:{a[0]}\nBrief: {a[1]}",
        from_="+13868543985",
        to="+48500076517"
    )
    print(message.status)

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

