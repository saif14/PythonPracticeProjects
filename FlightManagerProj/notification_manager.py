import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


class NotificationManager:
    def __init__(self):
        self.MAIL_ID = os.getenv("GMAIL_ID")
        self.MAIL_KEY = os.getenv("GMAIL_API_KEY")

    def create_notification(self, price, dept_city, dept_iata, arrival_city, arrival_iata,
                            outbound_date, inbound_date):
        """It creates lowest price notification message"""

        msg = f"Lower price alert! Only GBP{price} to fly from {dept_city}-{dept_iata} to " \
              f"{arrival_city}-{arrival_iata}, " \
              f"from {outbound_date} to {inbound_date}"
        return msg

    def sendNotification(self, msg):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.MAIL_ID, password=self.MAIL_KEY)
            connection.sendmail(from_addr=self.MAIL_ID,
                                to_addrs="mahmud.saif@ymail.com",
                                msg=f"Subject:Flight Deal\n\n{msg}")
