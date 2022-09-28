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


# площа
s = round((a + b + c + d), 2)

# визначаю чи рівні діагоналі
x = math.sqrt(a ** 2 + b ** 2)
y = math.sqrt(c ** 2 + d ** 2)

# визначаю чи рівні протилежні сторони
if a == c and b == d:
    z = (a + c) - (b + d)


if x == y and z == 0:
    print('Введені вами данні говорять , що це - квадрат')
elif x == y and z != 0:
    print('Це прямокутник і його площа складає', s, 'см')
else:
    print('Введені вами данні показують, що це чотирикутник, але не прямокутник і його площа складає', s, 'см')


























