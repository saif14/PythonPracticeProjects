from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_row()

for data in sheet_data:
    iataCode = flight_search.get_iata_code(data["city"])
    data_manager.update_row_data(column_name='iataCode', row_id=data['id'], updated_value=iataCode)
    pass


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.