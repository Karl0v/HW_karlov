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
add - для запису нотатки натисніть
earliest - для відображення від найранішої до найпізнішої
latest - для відображення від найпізнішої до найранішої 
longest - для відображення від найдовшої до найкоротшої
shortest - для відображення від найкоротшої до найдовшої
info - можливості програми
exit - вихід з програми''')




info()
notes = 'Notepad'





def loading():
    """
    Завантаження збережених нотаток зі службового файла
    :return: Показ нотаток
    """
    with open(notes, mode='r') as fp:
        print(fp.read())


def bylength():
    """
       Рахує кількість заповнених строк
       :return: Показує результат"""
    with open(notes, mode='r') as fp:
        return len(fp.readlines())


def add():
    """
Перепитує у користувача чи він дійсно хоче стерти вказану кількість заповнених нотаток новою
    :return: або записую нову, або виходить на початок
    """
    choise = input(f'\nЦя нотатка перезапише всі {bylength()} попередні \nВи впевнені???\ny/n >>> ')
    if choise == 'y':
        with open(notes, mode='w') as fp:
            s = (input('Нотатка >>> '))
            fp.write(s + '\n')
    elif choise != 'y':
        return


def save():
    """
    Приймає у користувача інформацію і записує її у файл
    :return: робить запис
    """
    with open(notes, mode='a') as fp:
        s = (input('Нотатка >>> '))
        fp.write(s + '\n')


def latest():
    """
    Відображення наповнення файла від найпізнішої до найранішої нотатки

    :return: відображає результат
    """
    with open(notes, mode='r') as fp:
        for text in reversed(list(fp)):
            print(text.strip('\n'))



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
    try:
        ask = input(f'Нотаток записано - {bylength()}, Ви впевнені, що хочете видалити файл  y/n?\n >>> ')
        if ask == 'y':
            os.remove(notes)
            print('\nВаш файл було видалено\n')
        elif ask == 'n':
            return
    except FileNotFoundError:
        print('\nВидалення не існуючого файлу не можливо\n')



while True:
    user_choice = input('''
Яку дію бажаєте виконати: save > load > clear > add > earliest > latest > longest > shortest > info > exit >> ''')
    try:
        if user_choice.lower() == 'save':
            save()
        elif user_choice == 'add':
            add()
        elif user_choice.lower() == 'load':
            loading()
        elif user_choice.lower() == 'earliest':
            loading()
        elif user_choice.lower() == 'latest':
            latest()
        elif user_choice.lower() == 'longest':
            longest()
        elif user_choice.lower() == 'shortest':
            shortest()
        elif user_choice.lower() == 'info':
            info()
        elif user_choice.lower() == 'clear':
            clear()
        elif user_choice.lower() == 'info':
            info()
        elif user_choice.lower() == 'exit':
            break
        else:
            print('Виберіть дію з списку')
    except FileNotFoundError:
        print('\nЗавантажити нотатки не виходить, так як файл з ними був видалений\n')








