# program generate password
# author: kra53n
# date: 23.06.20

from random import randrange, choice

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

    print('\nПороль уже сгенерирован, и он внизу:')
    print(password)

def gen_letter(digit = 'n'):
    letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    letters = letters.split(',')
    if digit == 'y':
        letter = randrange(10) + 1
        letter = str(letter)
        letters.append(letter)
    letter = choice(letters)
    
    cap = randrange(2)
    if cap == 0:
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
