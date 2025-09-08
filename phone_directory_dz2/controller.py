from model import PhoneBook, Contact


class PhoneBookController:
    def __init__(self):
        self.phonebook = PhoneBook()

    def add_contact(self, name, cell_number, email, telegram, comment):
        """
        Добавить контакт
        """
        contact = Contact(name, cell_number, email, telegram, comment)
        return self.phonebook.add_contact(contact)

    def find_contact(self, name):
        """
        Поиск по имени
        """
        return self.phonebook.find_contacts(name)

    def change_contact(self, contact_id, new_data):
        """
        Изменяет контакт через модель
        """
        return self.phonebook.update_contact(contact_id, new_data)

    def delete_contact(self, name):
        """
        Удаляет контакт через модель
        """
        return self.phonebook.delete_contact(name)


    def clear_phonebook(self):
        """
        Чистит книгу
        """
        return self.phonebook.delete_phone_book()

