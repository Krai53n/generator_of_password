from gen_pass import password


def ask_yes_no(question):
    while 1:
        yes_no = input('{} (y/n) '.format(question))
        yes_no = yes_no.lower()
        if (yes_no == 'y') or (yes_no == 'n'):
            break
    return yes_no


def digit(question):
    while 1:
        num = input(question)
        try:
            num = int(num)
        except ValueError:
            continue
        if num == int(num):
            break
    return num


if __name__ == '__main__':
    symbols = digit('Сколько симовлов ты хочешь иметь? ')
    symbols = int(symbols)
    # first letter with upper or lower
    f_upper = ask_yes_no('Хочешь, чтобы первая буква была заглавной?')
    # digits in password or not
    w_dig = ask_yes_no('Хочешь, чтобы у тебя были цифры?')

    pas = password(symbols, f_upper, w_dig)
    print('\nПароль уже сгенерирован, и он внизу:')
    print(pas)
