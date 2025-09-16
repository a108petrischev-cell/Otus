import json


class Contact:
    last_id = 1

    def __init__(self, name, cell_number, email, telegram, comment):
        Contact.last_id += 1
        self.id = Contact.last_id
        self.name = name
        self.cell_number = cell_number
        self.email = email
        self.telegram = telegram
        self.comment = comment

    def to_dict(self):
        """
        Функция добавляет контакт в словарь
        """

        return {
            "id": self.id,
            "name": self.name,
            "cell_number": self.cell_number,
            "email": self.email,
            "telegram": self.telegram,
            "comment": self.comment
        }


class PhoneBook:
    def __init__(self, filename="contacts.json"):
        self.contacts = []
        self.filename = filename
        self.load_from_file()

    def load_from_file(self):
        """
        Возвращает содержимое файла
        """
        try:
            with open(self.filename, 'r', encoding="utf-8") as file:
                self.contacts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []
            with open(self.filename, 'w', encoding="utf-8") as file:
                json.dump(self.contacts, file, indent=4, ensure_ascii=False)
            print("Файл не найден. Телефонная книга создана!")
        return self.contacts

    def save_to_file(self):
        """
        Сохраняет в файл в JSON
        """
        with open(self.filename, "w", encoding='utf-8') as file:
            json.dump(self.contacts, file, indent=4, ensure_ascii=False)

    def add_contact(self, contact: Contact):
        """
        Добавить контакт.
        Передаётся объект Contact, c добавлением наибольший id + 1.
        """
        if not self.contacts:
            new_id = 1
        else:
            new_id = max(contact["id"] for contact in self.contacts) + 1

        contact_dict = contact.to_dict()
        contact_dict["id"] = new_id

        self.contacts.append(contact_dict)
        self.contacts = sorted(self.contacts, key=lambda x: x['name'])
        self.save_to_file()
        print("Контакт успешно добавлен!")

    def find_contacts(self, name):
        """
        Найти контакт по имени
        """
        return [contact for contact in self.contacts if contact["name"] == name]

    def update_contact(self, contact_id, new_data: dict):
        """
        Обновить данные контакта по id.
        """
        for contact in self.contacts:
            if contact["id"] == contact_id:
                # обновляем только переданные поля
                for key, value in new_data.items():
                    if key in contact:
                        contact[key] = value
                self.save_to_file()
                return True
        return False

    def delete_contact(self, name):
        """
        Удалить контакт
        """
        new_contacts = [contact for contact in self.contacts if contact["name"] != name]
        if len(new_contacts) != len(self.contacts):
            self.contacts = new_contacts
            self.save_to_file()
            return True
        return False

    def delete_phone_book(self):
        """
        Удалить все контакты
        """
        self.contacts = []
        self.save_to_file()
        print("Все контакты удалены.")
