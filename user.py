import storage
class Person:
    def __init__(self, name):
        self.name = name

class User(Person):
    def __init__(self, name, user_id):
        super().__init__(name)
        self.user_id = user_id

    def __str__(self):
        return f"Name: {self.name}, User ID: {self.user_id}"
class UserManager:
    def __init__(self, storage_file='users.json'):
        self.storage_file = storage_file
        self.users = self.load_users()

    def load_users(self):
        users_data = storage.load_data(self.storage_file)
        return [User(**data) for data in users_data]

    def save_users(self):
        users_data = [user.__dict__ for user in self.users]
        storage.save_data(users_data, self.storage_file)

    def add_user(self, user):
        self.users.append(user)
        self.save_users()

    def list_users(self):
        for user in self.users:
            print(user)
