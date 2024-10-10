# main.py

from use_cases.create_user import CreateUserUseCase
from use_cases.update_user import UpdateUserUseCase
from infrastructure.repositories.user_repository import InMemoryUserRepository
from domain.value_objects.email import Email
from domain.entities.user import User


def main():
    # Set up repositories
    user_repository = InMemoryUserRepository()

    # Create Use Cases
    create_user_use_case = CreateUserUseCase(user_repository)
    update_user_use_case = UpdateUserUseCase(user_repository)

    # Create a new user
    print("Creating a new user...")
    user = create_user_use_case.execute(user_id=1, name="John Doe", email="john@example.com")
    print(f"User created: {user.name} with email {user.email}")

    # Update the user's email
    print("\nUpdating user's email...")
    updated_user = update_user_use_case.execute(user_id=1, new_email="john.doe@newdomain.com")
    print(f"User's updated email: {updated_user.email}")

    # List all users (in-memory example)
    print("\nListing all users...")
    all_users = user_repository.list_users()
    for user in all_users:
        print(f"User ID: {user.user_id}, Name: {user.name}, Email: {user.email}")


if __name__ == "__main__":
    main()
