#чотирикутники



import math

a = input('Введіть сторону a = ')
b = input('Введіть сторону b = ')
c = input('Введіть сторону c = ')
d = input('Введіть сторону d = ')

if a.isalpha() or b.isalpha() or c.isalpha() or d.isalpha():
    print('Введіть, будь ласка, цифри')
    a = float(input('Введіть сторону a = '))
    b = float(input('Введіть сторону b = '))
    c = float(input('Введіть сторону c = '))
    d = float(input('Введіть сторону d = '))
else:
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)


def square():
    if a == b == c == d:
        print('Введені вами данні говорять , що це - квадрат')
        exit(0)
square()

a = pow(a, 2)
b = pow(b, 2)
c = pow(c, 2)
d = pow(d, 2)


def area():
    s = round((a * b), 2)
    return s



def sqrt():
    x = math.sqrt(a + b)
    y = math.sqrt(c + d)
    if x == y:
        print('Це прямокутник і його площа складає', area(), 'см')
    else:
        print('Введені вами данні показують, що це чотирикутник, але не прямокутник')



print(sqrt())











