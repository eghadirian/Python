import random

def random_password(passlen):
    if passlen < 4 or passlen >12:
        print('The password length has to be at least 4 and not more than 12.')
        return ''
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    punc ='!@#$%^&*()?'
    r1 = random.randint(1, passlen-3)
    r2 = random.randint(1, passlen-r1-2)
    r3 = random.randint(1, passlen-r1-r2-1)
    r4 = passlen-r1-r2-r3
    a = random.sample(lowercase,r1)
    b = random.sample(uppercase, r2)
    c = random.sample(number, r3)
    d = random.sample(punc, r4)
    p =  list(''.join(a+b+c+d))
    index = [i for i in range(passlen)]
    random.shuffle(index)
    return ''.join([p[i] for i in index])

if __name__ == '__main__':
    print(random_password(int(input('Enter your desired password length, between 4 and 12:'))))