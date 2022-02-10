#Criar listas pares e inpares,
#Mostrar lista com os pares,
#Mostrar a Lista com os Impares:

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um Número: ')))
    resposta = str(input("Quer continuar? [S/N] "))
    if resposta in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A Lista completa é {num}')
print(f'A Lista de Pares é {pares}')
print(f'A Lista de impares é {impares}')
