# Конвертація валюти у гривню і навпаки
while True:

    a = input('''
        КУРС ВАЛЮТ:
    USD = 36.56 / 37.31
    EUR = 36.41 / 37.45

    Виберіть операцію яку хочете виконати, де:
    a - купити USD
    b - продати USD
    c - купити EUR
    d - продати EUR
     Ваш вибір - ''')

    if a.lower() != 'a' and a.lower() != 'b' and a.lower() != 'c' and a.lower() != 'd':
        continue

    c = input('Вкажіть суму для конвертації = ')
    try:
        int(c)
    except Exception:
        print('Вкажіть, будь ласка суму в цифрах')
        c = input('Вкажіть суму для конвертації = ')
    c = int(c)


    def sell_usd():
        print(int(36.56 * c), 'UAH')


    def buy_usd():
        print(int(c / 37.31), 'USD')


    def sell_eur():
        print(int(36.41 * c), 'UAH')


    def buy_eur():
        print(int(c / 37.45), 'EUR')


    if a == str('a'):
        buy_usd()
    elif a == str('b'):
        sell_usd()
    elif a == str('c'):
        buy_eur()
    elif a == str('d'):
        sell_eur()

    else:
        print('Щось пішло не так, спробуйте ще раз)')

    x = input('''
Щоб розпочати знову натисніть любу клавішу
   Якщо бажаєте закінчити натисніть - х
    ''')
    if x.lower() == 'x':
        break
    continue

