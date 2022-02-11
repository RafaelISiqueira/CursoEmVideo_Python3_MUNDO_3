#Criar uma função MAIOR() e receber varios parametros com valores inteiros. tem que analizar e dizer qual o maior
from time import sleep

def maior(*num):
    contador = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f'Foram informados {contador} Valores ao todo.')
    print(f'O maior valor, Informado foi {maior}.')


#Principal
maior(2, 9, 4, 2, 3)
maior(3)
maior(7, 9, 6)
maior(1, 3)
maior()
