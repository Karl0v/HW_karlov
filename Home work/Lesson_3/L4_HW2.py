# Bot

while True:
    question = input('Запитання - ')
    if 'привіт' in question.lower() or 'хай' in question.lower() or 'доброго дня' in question.lower():
        print('Доброго вечора, я бот з України!')
    elif 'як справи?' in question.lower() or 'що робиш?' in question.lower() or 'чим займаєшся?' in question.lower():
        print('Вчусь програмувати на Python!')
    elif 'фільм' in question.lower() or 'кінотеатр' in question.lower() or 'серіал ?' in question.lower():
        print('''
Соррі що втручаюсь, не знаю про що йде мова,
але подивіться серіал "WINNING TIME", він просто бомба!
''')
    elif 'бувай' in question.lower() or 'надобраніч' in question.lower() or 'гудбай' in question.lower() or 'до зустрічі' in question.lower():
        print("Побачимось у мережі, I'll be back.")
        break
    else:
        print('Дуже цікаво, але, нажаль, ніфіга не зрозуміло :(')
    continue
