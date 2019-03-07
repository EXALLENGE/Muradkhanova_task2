import random

f = ['h', 'e', 'l', 'l']
c = ['h', 'o', 'p', 'e', 'l', 'e', 's', 's']
e = ['a', 'n', 'x', 'i', 'e', 't', 'y']
d = ['s', 'a', 'd', 'n', 'e', 's', 's']
s = ['a', 'n', 'g', 'e', 'l']
v = ['s', 'o', 'o', 'n']
g = [f, c, e, d, s, v]
a = random.choice(g)
b = ['*' for i in a]
mistake = 0
while mistake < 5:
    print('Guess a letter:')
    x = input().lower()
    if x not in a:
        mistake += 1
        print('Missed, mistake', mistake, 'out of 5.')
        print('The word: ', *b, sep='')
    if x in a:
        for i in range(0, a.count(x)):
            k = a.index(x)
            b[k] = x
            a[k] = '+'
        print('Hit!')
        print('The word: ', *b, sep='')
    if '*' not in b:
        print('You won!')
        break
    if mistake == 5:
        print('You lost!')
