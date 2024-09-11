
def send_email(message, recipient,  sender='university.help@gmail.com'):
    if ("@" not in (recipient or sender)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif ((".com" not in sender[-4:]) and ('.net' not in sender[-4:]) and ('.ru' not in sender[-3:]) or
          (".com" not in recipient[-4:]) and ('.net' not in recipient[-4:]) and ('.ru' not in recipient[-3:])):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif recipient == sender:
        print('Невозможно отправить письмо самому себе!')
    elif sender != 'university.help@gmail.com':
        print(f"Нестандартный отправитель! \n Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


def test_send_mail():
    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

test_send_mail()
