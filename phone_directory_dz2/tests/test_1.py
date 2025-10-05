import pytest
import json
from phone_directory_dz2.model import PhoneBook, Contact


def test_add_first_contact(temp_phone_book, contact_to_add):
    """
    Проверка добавления первого контакта в пустой справочник.
    """
    temp_phone_book.add_contact(contact_to_add)
    assert len(temp_phone_book.contacts) == 1
    added_contact = temp_phone_book.contacts[0]
    assert added_contact["name"] == "Иван"
    assert added_contact["cell_number"] == "7925236526"
    assert added_contact["email"] == "234@mail.ru"
    assert added_contact["telegram"] == "@ivan"
    assert added_contact["comment"] == "Test"
    assert added_contact["id"] == 1

    with open(temp_phone_book.filename, 'r', encoding='utf-8') as f:
        data_from_file = json.load(f)

    assert len(data_from_file) == 1
    assert data_from_file[0]["name"] == "Иван"
    assert data_from_file[0]["cell_number"] == "7925236526"
    assert data_from_file[0]["email"] == "234@mail.ru"
    assert data_from_file[0]["telegram"] == "@ivan"
    assert data_from_file[0]["comment"] == "Test"


def test_add_second_contact_and_sorting(temp_phone_book):
    """
    Проверка добавления второго контакта и сортировки.
    """
    contact1 = Contact("Савелий", "89093245", "", "", "")
    temp_phone_book.add_contact(contact1)
    contact2 = Contact("Artem", "2352345", "", "", "")
    temp_phone_book.add_contact(contact2)

    assert len(temp_phone_book.contacts) == 2
    second_contact = next(c for c in temp_phone_book.contacts if c['name'] == 'Artem')
    assert second_contact['id'] == 2
    assert temp_phone_book.contacts[0]["name"] == "Artem"
    assert temp_phone_book.contacts[1]["name"] == "Савелий"


def test_edit_contact(temp_phone_book, contact_to_add):
    """
    Проверка изменения контакта.
    """
    temp_phone_book.add_contact(contact_to_add)
    contact_id_to_edit = 1
    new_data = {
        "name": "Иван Иваныч Иванов",
        "cell_number": "89053434455"
    }

    result = temp_phone_book.update_contact(contact_id_to_edit, new_data)

    assert result is True

    with open(temp_phone_book.filename, 'r', encoding='utf-8') as f:
        data_from_file = json.load(f)
    assert data_from_file[0]["name"] == "Иван Иваныч Иванов"
    assert data_from_file[0]["cell_number"] == "89053434455"
    assert data_from_file[0]["email"] == "234@mail.ru" #не изменилась


def test_delete_contact(temp_phone_book, contact_to_add):
    """
    Удаление контакта.
    """
    temp_phone_book.add_contact(contact_to_add)
    assert len(temp_phone_book.contacts) == 1

    contact_name_to_delete = "Иван"
    result = temp_phone_book.delete_contact(contact_name_to_delete)

    assert result is True
    assert len(temp_phone_book.contacts) == 0
    with open(temp_phone_book.filename, 'r', encoding='utf-8') as f:
        data_from_file = json.load(f)
    assert len(data_from_file) == 0


def test_find_contacts_by_exact_name(temp_phone_book):
    """
    Проверка поиска контактов по имени.
    """
    temp_phone_book.add_contact(Contact("Ваня", "890523423", "", "", ""))
    temp_phone_book.add_contact(Contact("Петя", "8954234234", "", "", ""))
    temp_phone_book.add_contact(Contact("Семен Семеныч", "90234234", "", "", ""))

    search_results_1 = temp_phone_book.find_contacts("Ваня")
    assert len(search_results_1) == 1
    assert search_results_1[0]["name"] == "Ваня"

    search_results_2 = temp_phone_book.find_contacts("Петя")
    assert len(search_results_2) == 1
    assert search_results_2[0]["name"] == "Петя"

    search_results_none = temp_phone_book.find_contacts("Семен")
    assert len(search_results_none) == 0
