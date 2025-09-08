import json


def add_contact():
    '''
    функция добавления контакта в список contacts
    '''

    new_contact = {
        "name": input("Введите имя: ").title(),
        "cell_number": int(input("Введите номер телефона: ")),
        "email": input("Введите адрес эл.почты: "),
        "telegram": input("Введите telegram: "),
        "comment": input("Доп. информация: "),
    }

    directory = []

    with open("contacts.json", 'r', encoding='utf-8') as file:
        directory = json.load(file)

    directory.append(new_contact)

    with open("contacts.json", "w", encoding='utf-8') as file:
        sorted_contacts = sorted(directory, key=lambda x: x['name'])
        json.dump(sorted_contacts, file, indent=4,
                  ensure_ascii=False)

    print("Контакт добавлен!")
    return new_contact


def read_all_contact():
    '''
    функция выводит весь справочник
    '''

    with open("contacts.json", "r", encoding='utf-8') as file:
        for i in file.readlines():
            print(i.strip())


def find_contact():
    '''
    функция поиска контакта по имени
    '''

    name = input("Input name: ")

    with open("contacts.json", "r", encoding='utf-8') as file:
        directory = json.load(file)

        found_contacts = []
        for contact in directory:
            if contact["name"] == name:
                found_contacts.append(contact)

        if found_contacts:
            print("Найденные контакты:")
            for contact in found_contacts:
                print(json.dumps(contact, ensure_ascii=False, indent=2))
        else:
            print(f"Контакт '{name}' не найден.")


def delete_contact():
    '''
    Поиск и удаление контакта по имени
    '''

    name = input("Введите имя контакта для удаления: ")

    with open("contacts.json", "r", encoding='utf-8') as file:
        directory = json.load(file)

        # Сохраняем только те контакты, которые не нужно удалять
        original_length = len(directory)
        directory = [contact for contact in directory if contact["name"] != name]

    if len(directory) == original_length:
        print(f"Контакт'{name}' не найден.")
        return

    # Сохраняем обновленные данные
    with open("contacts.json", "w", encoding='utf-8') as file:
        json.dump(directory, file, ensure_ascii=False, indent=4)
    print(f"Все контакты с именем '{name}' удалены!")


def change_contact():
    '''
    Поиск и изменение атрибутов контакта
    '''

    name = input("Введите имя контакта, который хотите изменить: ").title()

    with open("contacts.json", 'r', encoding='utf-8') as file:
        directory = json.load(file)

    found_contacts = [contact for contact in directory if contact["name"] == name]

    if not found_contacts:
        print(f"Контакт '{name}' не найден.")
        return

    print("Найдены следующие контакты:")
    for i, contact in enumerate(found_contacts, 1):
        print(f"[{i}] {json.dumps(contact, ensure_ascii=False, indent=2)}")

    if len(found_contacts) > 1:
        try:
            choice = int(input("Выберите номер контакта для изменения: ")) - 1
            if not 0 <= choice < len(found_contacts):
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
                return
            contact_to_change = found_contacts[choice]
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число.")
            return
    else:
        contact_to_change = found_contacts[0]

    original_contact = contact_to_change.copy()

    while True:
        print("\nЧто вы хотите изменить?")
        print("1. Имя")
        print("2. Номер телефона")
        print("3. Адрес эл.почты")
        print("4. Telegram")
        print("5. Доп. информация")
        print("6. Сохранить изменения")
        print("7. Отменить")

        field_choice = input("Выберите опцию: ").strip()

        if field_choice == '1':
            contact_to_change["name"] = input("Введите новое имя: ").title()
        elif field_choice == '2':
            contact_to_change["cell_number"] = int(input("Введите новый номер телефона: "))
        elif field_choice == '3':
            contact_to_change["email"] = input("Введите новый адрес эл.почты: ")
        elif field_choice == '4':
            contact_to_change["telegram"] = input("Введите новый telegram: ")
        elif field_choice == '5':
            contact_to_change["comment"] = input("Введите новую доп. информацию: ")
        elif field_choice == '6':
            print("\nПодтверждение сохранения:")
            print("Старые данные:", json.dumps(original_contact, ensure_ascii=False, indent=2))
            print("Внесенные изменения:", json.dumps(contact_to_change, ensure_ascii=False, indent=2))
            confirm = input("Вы уверены, что хотите сохранить эти изменения? (да/нет): ").lower()
            if confirm == 'да':
                directory = [c for c in directory if c != original_contact]
                directory.append(contact_to_change)
                with open("contacts.json", "w", encoding='utf-8') as file:
                    sorted_contacts = sorted(directory, key=lambda x: x['name'])
                    json.dump(sorted_contacts, file, indent=4, ensure_ascii=False)
                print("Контакт успешно обновлен!")
                break
            else:
                print("Изменения отменены.")
                return
        elif field_choice == '7':
            print("Изменения отменены.")
            return
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


def main_menu():
    '''Главное меню'''

    choose_function = input('''Введите:
    1 - чтобы создать новый контакт
    2 - чтобы прочитать справочник
    3 - чтобы найти нужный контакт
    4 - чтобы изменить контакт
    5 - чтобы удалить контакт
    ''').strip()

    if choose_function == "1":
        add_contact()
    elif choose_function == "2":
        read_all_contact()
    elif choose_function == "3":
        find_contact()
    elif choose_function == "4":
        change_contact()
    elif choose_function == "5":
        delete_contact()
    else:
        print("Такого пункта меню нет в списке.")
        main_menu()


main_menu()
