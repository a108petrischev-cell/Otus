import json

# глобальные переменные
phone_directory = "contacts.json"  # путь к файлу

new_contact = {
    "name": input("Введите имя: "),
    "cell_number": int(input("Введите номер телефона: ")),
    "email": input("Введите адрес эл.почты: "),
    "telegram": input("Введите telegram: "),
    "comment": input("Доп. информация: "),
}

contacts = []  # создаем список


def add_contact():  # функция добавления контакта в список contacts
    import json

    with open(phone_directory, 'r', encoding='utf-8') as file:
        contacts = json.load(file)  # обращается к глобальной переменной

    contacts.append(new_contact)

    with open(phone_directory, "w", encoding='utf-8') as file:
        sorted_contacts = sorted(contacts, key=lambda x: x['name'])  # сортировка по имени в ABC
        json.dump(sorted_contacts, file, indent=4,
                  ensure_ascii=False)  # запись в файл формате json с отступами и кириллицей

    print("Контакт добавлен!")
    return new_contact


add_contact()  # добавить контакт


# READ ALL CONTACTS
def read_all_contact():
    with open(phone_directory, "r", encoding='utf-8') as file:
        for i in file.readlines():
            print(i.strip())


read_all_contact()  # Прочитать все контакты


# FIND CONTACT
def find_contact():
    name = input("Input name: ")

    with open(phone_directory, "r", encoding='utf-8') as file:
        data = json.load(file)

        found_contacts = []
        for contact in data:
            if contact["name"] == name:
                found_contacts.append(contact)

        if found_contacts:
            print("Найденные контакты:")
            for contact in found_contacts:
                print(json.dumps(contact, ensure_ascii=False, indent=2))
        else:
            print(f"Контакт '{name}' не найден.")


find_contact()  # найти контакт


# DEL
def delete_contact():
    name = input("Введите имя контакта для удаления: ")

    with open(phone_directory, "r", encoding='utf-8') as file:
        data = json.load(file)

        # Сохраняем только те контакты, которые не нужно удалять
        original_length = len(data)
        data = [contact for contact in data if contact["name"] != name]

    if len(data) == original_length:
        print(f"Контакт'{name}' не найден.")
        return

    # Сохраняем обновленные данные
    with open(phone_directory, "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"Все контакты с именем '{name}' удалены!")


delete_contact()
