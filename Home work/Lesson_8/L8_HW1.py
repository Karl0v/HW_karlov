import os

def info():
    """
 Функція нагадує користувачу про можливості програми
    :return: виводить на екран можливості
    """
    info = '''Що вміє ця програма:
save - зберігає всі активні нотатки у службовий файл
load - завантаження збережених нотаток зі службового файла
clear - видалити всі збережені нотатки та видалити файл зберігання нотаток
info - можливості програми
exit - вихід з програми'''
    return print(info)


info()
notes = 'Notepad'


def note():
    """
    Приймає у користувача інформацію і записує її у файл
    :return: робить запис
    """
    with open(notes, mode='a+') as fp:
        s = (input('Нотатка >>> '))
        fp.write(s + '\n')


def loading():
    """
    Завантаження збережених нотаток зі службового файла
    :return: Показ нотаток
    """
    with open(notes, mode='r') as fp:
        print(fp.read())


def remove():
    """
    Видаляє всі збережені нотатки та сам файл зберігання нотаток
    :return: видалення
        """
    os.remove(notes)



while True:
    user_choise = input('Яку дію бажаєте виконати: > note > load > clear > info > exit >> ')
    if user_choise.lower() == 'note':
        note()
    elif user_choise.lower() == 'load':
        try:
            loading()
        except FileNotFoundError:
            print('\nЗавантажити нотатки не виходить, так як файл з ними був видалений\n')
    elif user_choise.lower() == 'clear':
        try:
            ask = input('Ви впевнені, що хочете видалити файл y/n?\n >>> ')
            if ask == 'y':
                remove()
                print('\nВаш файл було видалено\n')
        except FileNotFoundError:
            print('\nВидалення не існуючого файлу не можливо\n')
    elif user_choise.lower() == 'info':
        info()
    elif user_choise.lower() == 'exit':
        break
    else:
        print('Виберіть дію з списку')









