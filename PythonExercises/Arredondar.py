import math
num = float(input('Insira um numero com virgula: '))
arre = math.floor(num)
print('O numero arredondado é:{} '.format(arre))

print('O numero é {} e sua parte inteira é {}'.format(num, math.trunc(num)))

print('O numero é {} e sua porção inteira é {}'.format(num, int(num)))