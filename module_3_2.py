def send_email (message, recipient, sender = "university.help@gmail.com"):
    def valid_address(address):
        return ("@" in address and (address.endswith(".com") or address.endswith(".ru") or address.endswith(".net")))

    if not valid_address(recipient)  or not valid_address(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}. Один из адресов неверен.')
        return
    if sender == recipient:
        print ('Нельзя отправить письмо самому себе!')
        return
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Вам письмо, не требующее ответа', 'post@server.net')
send_email('Не ку-ку!', 'postserver.net')
send_email('Да без разницы...', 'certain@postserver.net', "shyshel@myshel.ru")
send_email('Да без разницы...', 'university.help@gmail.com')