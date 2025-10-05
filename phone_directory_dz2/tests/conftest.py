import pytest
from phone_directory_dz2.model import PhoneBook, Contact

@pytest.fixture
def temp_phone_book(tmp_path):
    """
    Фикстура для создания временного экземпляра PhoneBook
    с временным файлом контактов.
    """
    temp_file = tmp_path / "test_contacts.json" #из pathlib, чтобы обнулять содержание
    book = PhoneBook(filename=str(temp_file))
    book.contacts = []
    return book

@pytest.fixture
def contact_to_add():
    contact_to_add = Contact(
        name="Иван",
        cell_number="7925236526",
        email="234@mail.ru",
        telegram="@ivan",
        comment="Test"
    )
    return contact_to_add