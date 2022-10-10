import os
from dotenv import load_dotenv
import requests
import smtplib



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv()
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
MAIL_ID = "parvezsaifmahmud@gmail.com"
MAIL_KEY = os.getenv("GMAIL_API_KEY")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"


def send_mail(news_message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MAIL_ID, password=MAIL_KEY)
        connection.sendmail(from_addr=MAIL_ID,
                            to_addrs="mahmud.saif@ymail.com",
                            msg=f"Subject:News\n\n{news_message}")



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

difference_percentage = abs(
    yesterday_closing_price - day_before_yesterday_closing_price) / yesterday_closing_price * 100
print(difference_percentage)


def get_news():
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        # "language": "en"
    }
    news_response = requests.get(url=NEWS_API_ENDPOINT, params=news_params)
    return news_response.json()["articles"]


if difference_percentage >= 5:
    news_data = get_news()
    three_articles = news_data[:3]
    # print(three_articles)
    formatted_article_list = [f"Headline: {article['title']}. \nBrief: {article['content']}" for article in three_articles]

    for article in formatted_article_list:
        # news_msg = article
        news_msg = u''.join((article)).encode('utf-8').strip()
        print("NES MSG")
        send_mail(news_msg)

else:
    print("NO NEWS")



"""
Instead of sending sms, I sent mail. Twillio is a shit
"""

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
