from domain.value_objects.email import Email


class User:
    def __init__(self, user_id: int, name: str, email: Email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def change_email(self, new_email: Email):
        self.email = new_email

    def deactivate_account(self):
        # Logic to deactivate the user account
        pass

    def __eq__(self, other):
        return self.user_id == other.user_id
