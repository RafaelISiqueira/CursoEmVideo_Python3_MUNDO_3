#criar valores unicos para uma lista, e mostrar em ordem crescente:
numeros = list()
while True:
    n = int(input('Digite o valor de um Número inteiro: '))
    if n not in numeros:
        numeros.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("valor duplicado! Não vou adicionar...")
    r = str(input("Quer continuar? [S/N] "))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Você digitou os valores {numeros} ')
