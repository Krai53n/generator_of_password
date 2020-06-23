# program generate password
# author: kra53n
# date: 32.06.20

from random import randrange, choice

def main():
    symbols = digit('Сколько симовлов ты хочешь иметь? ')
    symbols = int(symbols)
    f_upper = ask_yes_no('Хочешь, чтобы первая буква была заглавной?')
    w_dig = ask_yes_no('Хочешь, чтобы у тебя были цифры?')
    password = ''

    for i in range(symbols):
        if i == 0:
            if f_upper == 'y':
                password += (gen_letter()).upper()
        else:
            password += gen_letter(w_dig)

    print('\nПороль уже сгенерирован, и он внизу:')
    print(password)

def gen_letter(digit = 'n'):
    letters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    letters = letters.split(',')
    letter = randrange(10) + 1
    letter = str(letter)
    letters.append(letter)
    letter = choice(letters)
    
    cap = randrange(2)
    if cap == 0:
        letter = letter.capitalize()
    return letter

def ask_yes_no(question):
    yes_no = None
    while yes_no != 'y' or 'n':
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
