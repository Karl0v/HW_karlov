# Відрізання останніх цифр від числа, результат - число без відрізаного


def in_put():
    a = input('введіть число = ')
    if not a.isnumeric():
        print('Введіть будь ласка число цифрами')
        a = input('введіть число = ')

    b = input('скільки символів треба відрізати з права = ')
    if not b.isnumeric():
        print('Введіть будь ласка число цифрами')
        b = input('скільки символів треба відрізати з права = ')
    return print(a[:-int(b)])

in_put()

while True:
    x = input('''
        Щоб розпочати знову натисніть любу клавішу
           Якщо бажаєте закінчити натисніть - х
            ''')
    if x.lower() == 'x':
        break
    continue