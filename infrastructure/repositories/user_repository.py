# InMemoryUserRepository is a simple implementation for testing purposes.
class InMemoryUserRepository:
    def __init__(self):
        self.users = {}

    def save(self, user):
        self.users[user.user_id] = user

    def find_by_id(self, user_id):
        return self.users.get(user_id)

    def list_users(self):
        return list(self.users.values())
