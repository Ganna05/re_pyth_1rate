# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.


# desicion of 1-st task
'''
Проверяет корректность занесенных данных
f_name и f_surname - Должны быть с загловной буквы
f_email - не должен содержать заглавных букв, и должен быть в формате:
  текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru|org|com
На вход передаются параменты (имя, фамилия, e-mail, шаблон email)
'''
def data_control(f_name, f_surname, f_email, patt):
    a = []
    st_fio_eng = '^[A-Z][a-z]+$' #рег.выражение для фио на латинице
    st_fio_rus = '^[А-Я][а-я]+$' #рег.выражение для фио на кириллице
    if re.search(st_fio_eng, name) == None and re.search(st_fio_rus, name) == None:
        a.append("Имя")
    if re.search(st_fio_eng, surname) == None and re.search(st_fio_rus, surname) == None:
        a.append("Фамилия")
    if re.search(patt, f_email) == None:
        a.append("email")
    if a != []:
        a.insert(0, 0)
    else:
        a = [1]
    return a


name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
email = input('Ваш email: ')

import re

pattern1 = '^[a-z_0-9]+@[a-z0-9]+\.(ru|com|org)$' #рег.выражение для e-mail
b = data_control(name, surname, email, pattern1)
print("Добро пожаловать, {} {}. Ваш e-mail: {} - корректен".format(surname, name, email)
      if b[0] else "Неверно занесено: ", str(b[1:]))
