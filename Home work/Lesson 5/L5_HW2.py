# офіційне письмо

email = '''Dear *Ім'я одержувача* *Прізвище одержувача*,
   
  We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum in faucibus massa. 
  Suspendisse at ex varius, porttitor eros sit amet, sagittis nibh. In vel est a tortor tempor luctus a. 
   
  ________________
  *Ім'я відправика* *Прізвище відправника*
  *Посада відправника*'''

name_recipient = input("Введіть, будь ласка, Ім'я одержувача >> ")
lastname_recipient = input("Введіть, будь ласка, Прізвище одержувача >> ")
name_sender = input("Введіть, будь ласка, Ім'я відправника >> ")
lastname_sender = input("Введіть, будь ласка, Прізвище відправника >> ")
position_sender = input("Введіть, будь ласка, Посаду відправника >> ")

def paste(email):
    a = email.replace("*Ім'я одержувача*", name_recipient.capitalize())
    b = a.replace("*Прізвище одержувача*", lastname_recipient.capitalize())
    c = b.replace("*Ім'я відправика*", name_sender.capitalize())
    d = c.replace("*Прізвище відправника*", lastname_sender.capitalize())
    e = d.replace("*Посада відправника*", position_sender.capitalize())
    return print(e)


paste(email)