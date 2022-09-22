# офіційне письмо
while True:

    name_recipient = input("Введіть, будь ласка, Ім'я одержувача >> ")
    lastname_recipient = input("Введіть, будь ласка, Прізвище одержувача >> ")
    name_sender = input("Введіть, будь ласка, Ім'я відправника >> ")
    lastname_sender = input("Введіть, будь ласка, Прізвище відправника >> ")
    position_sender = input("Введіть, будь ласка, Посаду відправника >> ")

    email = f'''
Dear {name_recipient.capitalize()} {lastname_recipient.capitalize()},

We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in faucibus massa.
Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. In vel est a tortor tempor luctus a.

________________
{name_sender.capitalize()} {lastname_sender.capitalize()},
{position_sender.capitalize()}'''

    print(email)

    x = input('''
            Щоб розпочати знову натисніть любу клавішу
               Якщо бажаєте закінчити натисніть - х
                >> ''')
    if x.lower() == 'x':
        break
    continue