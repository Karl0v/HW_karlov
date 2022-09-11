# конвертація долара в гривню

x = 36.83
q = input('введіть суму в USD = ')
try:
    int(q)
except Exception:
    print('Вкажіть, будь ласка суму в цифрах')
    q = input('введіть суму в USD = ')


print('Мажор, в тебе аж цілих',round(float(q) * x, 2),'UAH')
