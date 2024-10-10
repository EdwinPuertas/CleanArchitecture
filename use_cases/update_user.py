# use_cases/update_user.py

from domain.value_objects.email import Email

class UpdateUserUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user_id, new_email):
        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found")

        user.change_email(new_email)  # Pass string directly
        self.user_repository.save(user)
        return user
