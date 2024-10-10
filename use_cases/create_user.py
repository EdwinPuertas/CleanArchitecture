# CreateUserUseCase is responsible for creating new users.
from domain.entities.user import User
from domain.value_objects.email import Email

class CreateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id, name, email):
        user = User(user_id, name, Email(email))
        self.user_repository.save(user)
        return user
