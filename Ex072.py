#Criar um programa que leia o nome de um numero de 0 a 20:

contador = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onde', 'dose', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', "vinte")

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {contador[num]}')
    elif num > 20:
        break
    else:
        print('Números negativos invalidos, Tente Novamente. ')
print('-='*20)
print('Programa finalizado com sucesso!!!')