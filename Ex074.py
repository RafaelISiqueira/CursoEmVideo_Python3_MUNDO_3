#Randomizar numeros de 1,10 e mostrar Maior e menor valor:

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO MAIOR valor sorteado foi {max(numeros)}')
print(f'O MENOR valor sorteado foi {min(numeros)}')
