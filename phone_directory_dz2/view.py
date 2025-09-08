from controller import PhoneBookController


def main_menu():
    controller = PhoneBookController()

    while True:
        print("\nТелефонный справочник:")
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Показать все контакты")
        print("6. Очистить телефонную книгу")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Имя: ")
            cell_number = input("Телефон: ")
            email = input("Email: ")
            telegram = input("Telegram: ")
            comment = input("Комментарий: ")
            if controller.add_contact(name, cell_number, email, telegram, comment):
                print("Контакт добавлен")

        elif choice == "2":
            name = input("Введите имя для поиска: ")
            results = controller.find_contact(name)
            if results:
                print("Найдено:", results)
            else:
                print("Контакт не найдено")

        elif choice == "3":
            change_contact_view(controller)

        elif choice == "4":
            name = input("Введите имя для удаления: ")
            if controller.delete_contact(name):
                print("Контакт удалён")
            else:
                print("Контакт не найден")

        elif choice == "5":
            contacts = controller.phonebook.contacts
            if contacts:
                for contact in contacts:
                    print(contact)
            else:
                print("Книга пуста")

        elif choice == "6":
            controller.clear_phonebook()
            print("Все контакты удалены")

        elif choice == "0":
            print("Выход")
            break

        else:
            print("Нет такого пункта, попробуйте ещё раз")

def change_contact_view(controller):
    name = input("Введите имя контакта для изменения: ").title()
    found_contacts = controller.find_contact(name)

    if not found_contacts:
        print(f"Контакт '{name}' не найден.")
        return

    print("Найдены следующие контакты:")
    for i, contact in enumerate(found_contacts, 1):
        print(f"[{i}] {contact}")

    if len(found_contacts) > 1:
        choice = int(input("Выберите номер контакта: ")) - 1
        contact_to_change = found_contacts[choice]
    else:
        contact_to_change = found_contacts[0]

    new_data = {}
    while True:
        print("\nЧто вы хотите изменить?")
        print("1. Имя")
        print("2. Телефон")
        print("3. Email")
        print("4. Telegram")
        print("5. Комментарий")
        print("6. Сохранить и выйти")
        print("7. Отмена")

        choice = input("Выберите опцию: ")

        if choice == "1":
            new_data["name"] = input("Новое имя: ").title()
        elif choice == "2":
            new_data["cell_number"] = input("Новый телефон: ")
        elif choice == "3":
            new_data["email"] = input("Новый email: ")
        elif choice == "4":
            new_data["telegram"] = input("Новый telegram: ")
        elif choice == "5":
            new_data["comment"] = input("Новый комментарий: ")
        elif choice == "6":
            if controller.change_contact(contact_to_change["id"], new_data):
                print("Контакт обновлен!")
            else:
                print("Ошибка при обновлении.")
            break
        elif choice == "7":
            print("Отмена.")
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main_menu()

