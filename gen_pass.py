from random import choice, randrange
from string import digits, ascii_lowercase


def gen_letter(digit = 'n'):
    '''
    Function generate random letter and give this letter to
    password function
    '''
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


def password(symbols = 15, first_letter = 'y', digits = 'y'):
    '''
    Function generate password with your length of symbols,
    capital letter in the start of password, digits if you whant
    '''
    pas = ''
    for i in range(symbols):
        if i == 0:
            pas += gen_letter()
            if first_letter == 'y':
                pas = pas.upper()
            continue
        pas += gen_letter(digits)

    return pas
