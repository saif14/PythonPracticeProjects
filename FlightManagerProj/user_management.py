from data_manager import DataManager

data_manager = DataManager()

class UserManagement:
    def __init__(self):
        self.first_name: str = None
        self.last_name: str = None
        self.email: str = None

    def add_user(self):
        self.first_name = input("Enter First Name: ")
        self.last_name = input("Enter Last Name: ")
        self.email = input("Enter email:")
        data = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email
        }

        data_manager.post_row_data(sheet="users", data=data)


    def get_all_users(self):
        all_user = data_manager.get_rows(sheet="users")
        return all_user
