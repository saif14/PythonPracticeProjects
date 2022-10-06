import os
from dotenv import load_dotenv
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])
print(yesterday_closing_price)


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_price)

difference_percentage = abs(yesterday_closing_price - day_before_yesterday_closing_price)/yesterday_closing_price*100
print(difference_percentage)

if difference_percentage >= 2:
    print("BIG NEWS")
else:
    print("NO NEWS")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    news_params = {
        "q":"",
        "from":"",
        "apiKey": NEWS_API_KEY
    }

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

