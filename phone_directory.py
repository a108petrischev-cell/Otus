# ADD CONTACT
import json


def add_contact():
    import json
    new_contact = {
        "name": input("Input name: "),
        "cell_number": int(input("Input cell number: ")),
        "email": input("Input email: "),
        "telegram": input("Input telegram: "),
        "comment": input("Input comment: "),
    }

    book_of_contacts = "contacts.json"
    contacts = []

    with open(book_of_contacts, 'r', encoding='utf-8') as file:
        contacts = json.load(file)

    contacts.append(new_contact)

    with open(book_of_contacts, "w", encoding='utf-8') as file:
        json.dump(contacts, file, indent=4, ensure_ascii=False)

    print("Контакт добавлен!")
    return new_contact


# add_contact()  # добавить контакт

# READ ALL CONTACTS


def read_all_contact():
    with open("contacts.json", "r", encoding='utf-8') as file:
        for i in file.readlines():
            print(i.strip())
        # data = json.load(file)
        # print(data)


# read_all_contact() # Прочитать все контакты


def find_contact():
    name = input("Input name: ")

    try:
        with open("contacts.json", "r", encoding='utf-8') as file:
            data = json.load(file)

            found_contacts = []
            for contact in data:
                if contact["name"].lower() == name.lower():
                    found_contacts.append(contact)

            if found_contacts:
                print("Найденные контакты:")
                for contact in found_contacts:
                    print(json.dumps(contact, ensure_ascii=False, indent=2))
            else:
                print(f"Контакт с именем '{name}' не найден.")

    except FileNotFoundError:
        print("Файл contacts.json не найден.")
    except json.JSONDecodeError:
        print("Ошибка чтения JSON файла.")

# find_contact() # найти контакт
