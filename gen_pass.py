# program generate password
# author: kra53n
# date: 23.06.20


from random import randrange, choice
from string import digits, ascii_lowercase


def main():
    '''
    Function which run all program
    '''
    # lenght of password
    symbols = digit('Сколько симовлов ты хочешь иметь? ')
    symbols = int(symbols)
    # first letter with upper or lower
    f_upper = ask_yes_no('Хочешь, чтобы первая буква была заглавной?')
    # digits in password or not
    w_dig = ask_yes_no('Хочешь, чтобы у тебя были цифры?')
    password = ''

    # generate password
    for i in range(symbols):
        if i == 0:
            if f_upper == 'y':
                password += (gen_letter()).upper()
            else:
                password += (gen_letter()).lower()
        else:
            password += gen_letter(w_dig)

    print('\nПароль уже сгенерирован, и он внизу:')
    print(password)


def gen_letter(digit = 'n'):
    letters = ascii_lowercase
    if digit == 'y':
        letter = digits
        letter = str(letter)
        letters += letter
    letter = choice(letters)
    
    capital_letter = randrange(2)
    if capital_letter == 0:
        letter = letter.capitalize()
    return letter


def ask_yes_no(question):
    while 1:
        yes_no = input('{} (y/n) '.format(question))
        yes_no = yes_no.lower()
        if yes_no == 'y' or 'n':
            break
    return yes_no


def digit(question):
    num = '1'
    while num != int(num):
        num = input(question)
        num = int(num)
    return num


main()
