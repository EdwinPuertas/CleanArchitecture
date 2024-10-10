import pytest
from domain.entities.user import User

def test_change_email():
    user = User(1, "John Doe", "john@example.com")
    user.change_email("new_email@example.com")
    assert user.email == "new_email@example.com"

def test_invalid_email_change():
    user = User(1, "John Doe", "john@example.com")
    with pytest.raises(ValueError):
        user.change_email("invalid-email")
