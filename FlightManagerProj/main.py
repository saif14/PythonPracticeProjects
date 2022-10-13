from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

sheet_data = data_manager.get_row()
#
"""Updating the IATA code for each city in the google sheet"""
# for data in sheet_data:
#     iataCode = flight_search.get_iata_code(data["city"])
#     data_manager.update_row_data(column_name='iataCode', row_id=data['id'], updated_value=iataCode)
#     pass

"""Getting the price of journey and sending notification"""
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
        notification_manager.sendNotification(msg)

