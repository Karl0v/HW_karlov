# градуси в радіани
import math
while True:
    a = math.pi / 180

    b = input('''
        Виберіть операцію яку хочете виконати, де:
        a - конвертувати в радіани
        b - конвертувати в градуси
            Ваш вибір - ''')

    if b != 'a' and b != 'b':
        continue

    c = input('введіть необхідне число = ')
    try:
        float(c)
    except Exception:
        print('Вкажіть, будь ласка суму в цифрах')
        c = input('введіть необхідне число = ')
    c = float(c)

    def radian_to_degree():
        print(round((a * c), 2),'Радіан')

    def degree_to_radian():
        print(round((c / a), 2), 'Градуси')

    if b == 'a':
        radian_to_degree()
    elif b == 'b':
        degree_to_radian()
    else: print('Щось пішло не так, спробуйте ще раз')

    x = input('''
    Щоб розпочати знову натисніть любу клавішу
       Якщо бажаєте закінчити натисніть - х
        ''')
    if x.lower() == 'x':
        break
    continue




