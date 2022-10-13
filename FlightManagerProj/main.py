from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from user_management import UserManagement

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()
user_management = UserManagement()

sheet_data = data_manager.get_rows(sheet="prices")
#
"""Updating the IATA code for each city in the google sheet"""
# for data in sheet_data:
#     iataCode = flight_search.get_iata_code(data["city"])
#     data_manager.update_row_data(sheet="prices", column_name='iataCode', row_id=data['id'], updated_value=iataCode)
#     pass


"""adding a new user"""
# user_management.add_user()

"""fetching all the user data"""
all_user_data = user_management.get_all_users()
print(all_user_data)


"""Getting the price of journey and sending notification to all users"""
for data in sheet_data:
    # print(data)
    sheet_price = data['lowestPrice']
    price, journey_data = flight_data.get_price(data["iataCode"])
    print(f"{data['city']} {price} {journey_data}")
    if price < sheet_price:
        msg = notification_manager.create_notification(
            price=price,
            dept_city="London",
            dept_iata=journey_data['fly_from'],
            arrival_city=data['city'],
            arrival_iata=data['iataCode'],
            outbound_date=journey_data['date_from'],
            inbound_date=journey_data['date_to']
        )
        print(msg)
        for user in all_user_data:
            notification_manager.sendNotification(msg, user["email"])

