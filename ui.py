def choice_operation():
    print('''Выберете вариант использования справочника: \n1 - Добавить человека \n2 - Просмотр справочника \n3 - Импорт данных из файла \n4 - Экспорт данных в файл \n5 - Выход''')
    operation = correct_input(('1', '2', '3', '4', '5'))
    return operation

def correct_input(num):
    error = True
    while error:
        choise = input('Ваш выбор: ')
        if choise in num:
            error = False
        else:
            print('Некорректный выбор, повторите ввод')
    return choise

def input_user():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    description = input('Введите описание: ')
    return [surname, name, phone, description]

def repeat_input():
    print('Вы хотите добавить еще контакт? Да/Нет')
    return correct_input(('Да', 'Нет'))
