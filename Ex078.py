#faça uma lista para preencher, diga os numeros digitados, liste o maior e menor e mostre a posição
listanum = []
maior = 0
menor = 0

for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('='*48)
print(f'Você digitou os números: {listanum}')
print(f'O maior Número digitado foi {maior}! ', end=' ')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'na posição: {i}.')
print()
print(f'O menor Número digitado foi {menor}! ', end=' ')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'na posição: {i}.')
print()
print('='*48)
