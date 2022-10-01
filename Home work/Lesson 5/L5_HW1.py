#чотирикутники



import math

while True:
    a = input('Введіть сторону a = ')
    b = input('Введіть сторону b = ')
    c = input('Введіть сторону c = ')
    d = input('Введіть сторону d = ')
    if a.isnumeric() and b.isnumeric() and c.isnumeric() and d.isnumeric():
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        break

    else:
        print('Введіть, будь ласка, цифри')


def area(a,b): #функція вираховує площу прямокутника
    s = round(a * b), 2
    return s


def diagonal(a,b,c,d): #функція перевіряє рівність діагоналей
    if (a**2 + b**2) == (c**2 + d**2):
        return True


def sides_is_equal(a,b,c,d): #функція перевіряє рівність сторін
    if a == b == c == d:
        return True

if diagonal(a,b,c,d) is True and sides_is_equal(a,b,c,d) is True:
    print('Введені вами данні говорять , що це - квадрат')
elif diagonal(a,b,c,d) is True and sides_is_equal(a,b,c,d) is not True:
    print('Це прямокутник і його площа складає', area(a, b), 'см')
else:
    print('Введені вами данні показують, що це чотирикутник, але не прямокутник')
