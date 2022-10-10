import os


def info():
    """
 Функція нагадує користувачу про можливості програми
    :return: виводить на екран можливості
    """
    print('''
Що вміє ця програма:
save - зберігає всі активні нотатки у службовий файл
load - завантаження збережених нотаток зі службового файла
clear - видалити всі збережені нотатки та видалити файл зберігання нотаток
info - можливості програми
exit - вихід з програми''')


def infoin():
    print('''
Як ви бажаєте відобразити нотатки? 
Для запису нотатки натисніть - "Enter"
Для відображення від найранішої до найпізнішої - "earliest"
Для відображення від найпізнішої до найранішої - "latest"
Для відображення від найдовшої до найкоротшої - "longest"
Для відображення від найкоротшої до найдовшої - "shortest"
Якщо щось забули - "info"
Вийти - "x"''')


info()
notes = 'Notepad'


def save():
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


def latest():
    """
    Відображення наповнення файла від найпізнішої до найранішої нотатки

    :return: відображає результат
    """
    with open(notes, mode='r') as fp:
        for text in reversed(list(fp)):
            print(text.strip('\n'))


'''def bylength(notes):
    with open(notes, mode='r') as fp:
        for text in reversed(list(fp)):
            print(len(text))'''


def longest():
    """
      Відображення наповнення файла від найдовшої до найкоротшої

      :return: відображає результат
      """
    with open(notes, mode='r') as fp:
        for text in sorted(list(fp), key=len, reverse=True):
            print(text.strip('\n'))


def shortest():
    """
        Відображення наповнення файла від найкоротшої до найдовшої

        :return: відображає результат
        """
    with open(notes, mode='r') as fp:
        for text in sorted(list(fp), key=len, reverse=False):
            print(text.strip('\n'))


def clear():
    """
    Видаляє всі збережені нотатки та сам файл зберігання нотаток
    :return: видалення
        """
    os.remove(notes)


while True:
    user_choise = input('\nЯку дію бажаєте виконати: > save > load > clear > info > exit >> ')
    if user_choise.lower() == 'save':
        save()
    elif user_choise.lower() == 'load':
        infoin()
        while True:
            start = input('''
Для нотатки натисніть - "Enter"
або інший варіант -> ''')
            try:
                if start == '':
                    save()
                elif start.lower() == 'earliest':
                    loading()
                elif start.lower() == 'latest':
                    latest()
                elif start.lower() == 'longest':
                    longest()
                elif start.lower() == 'shortest':
                    shortest()
                elif start.lower() == 'info':
                    info()
                elif start.lower() == 'x':
                    break
                else:
                    print('Якщо щось забули - "i"')
                '''
                loading()'''
            except FileNotFoundError:
                print('\nЗавантажити нотатки не виходить, так як файл з ними був видалений\n')

    elif user_choise.lower() == 'clear':
        try:
            ask = input('Ви впевнені, що хочете видалити файл y/n?\n >>> ')
            if ask == 'y':
                clear()
                print('\nВаш файл було видалено\n')
        except FileNotFoundError:
            print('\nВидалення не існуючого файлу не можливо\n')
    elif user_choise.lower() == 'info':
        info()
    elif user_choise.lower() == 'exit':
        break
    else:
        print('Виберіть дію з списку')









