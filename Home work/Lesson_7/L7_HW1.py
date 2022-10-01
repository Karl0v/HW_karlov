#Нотатник
notes = []


def info():
    print('''Вас вітає нотатник! 
Для запису нотатки натисніть - "Enter"
Для відображення від найранішої до найпізнішої - "earliest"
Для відображення від найпізнішої до найранішої - "latest"
Для відображення від найдовшої до найкоротшої - "longest"
Для відображення від найкоротшої до найдовшої - "shortest"
Якщо щось забули - "i"
Вийти - "x"''')


def begin(notes):
   user = input('Нотатка >>> ')
   notes.append(user)
   return start

#відображення від найранішої до найпізнішої
def earliest(notes):
    for text in notes:
        print(text)

#відображення від найпізнішої до найранішої
def latest(notes):
    for text in notes[::-1]:
        print(text)


def bylength(notes):
       return len(notes)

#відображення від найдовшої до найкоротшої
def longest(notes):
    text = sorted(notes, key=len)
    print("\n".join(reversed(text)))

#відображення від найкоротшої до найдовшої
def shortest(notes):
    text = sorted(notes, key=len)
    print("\n".join(text))

#вихід
def finish():
    print(f'Нотаток записано - {len(notes)}')
    print('Гарного дня!!!')
    exit(0)


print('''Вас вітає нотатник! 
Для запису нотатки натисніть - "Enter"
Для відображення від найранішої до найпізнішої нотатки - "earliest"
Для відображення від найпізнішої до найранішої нотатки - "latest"
Для відображення від найдовшої до найкоротшої - "longest"
Для відображення від найкоротшої до найдовшої - "shortest"
Якщо щось забули - "i"
Вийти - "x"''')

while True:
    start = input('''Для нотатки натисніть - "Enter"
    або інший варіант -> ''')
    if start == '':
        begin(notes)
    elif start.lower() == 'earliest':
        earliest(notes)
    elif start.lower() == 'latest':
        latest(notes)
    elif start.lower() == 'longest':
        longest(notes)
    elif start.lower() == 'shortest':
        shortest(notes)
    elif start.lower() == 'i':
        info()
    elif start.lower() == 'x':
        finish()
    else:
        print('Якщо щось забули - "i"')








