# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number, *bank1):
    for person in bank1:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    else:
        return 'На вашем счету недостаточно средств!'


def type_change_float(str_in):
    try:
        return float(str_in)
    except ValueError:
        return 0
    except Exception as e:
        print(e.__class__)


def process_user_choice(choice, person):
    import re
    if choice == 1:
        print(check_account(person))
    elif choice == 2:
        count = type_change_float(input('Сумма к снятию:'))
        if count > 0:
            print(withdraw_money(person, count))
        else:
            print('Введена некорректная сумма. ', withdraw_money(person, 0))


def start():
    in_data = input('Введите номер карты и пин код через пробел:')
    if in_data == "":
        card_number, pin_code = 0, 0
    else:
        if in_data.find(' ') != 0 and len(in_data) >= 2 and in_data[-1] != ' ' and in_data[0] != ' ':
            card_number, pin_code = in_data.split()
        else:
            card_number = 0
            pin_code = 0
    card_number = int(type_change_float(card_number))
    pin_code = int(type_change_float(pin_code))
    person = get_person_by_card(card_number, *bank)
    if person and is_pin_valid(person, pin_code):
        while True:
            choice = int(input('Выберите пункт:\n'
                               '1. Проверить баланс\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '---------------------\n'
                               'Ваш выбор:'))
            if choice == 3:
                break
            elif choice == 2 or choice == 1:
                process_user_choice(choice, person)
    else:
        print('Номер карты или пин код введены не верно!')


start()
