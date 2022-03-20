#Leia 4 números,
#Quantas vezes apareceu 9.
#Em que posição estava o primeiro 3,
#mostrar os númeres pares digitados:

numero = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o ultimo número: ')))
print(f"Você digitou os valores: {numero}")
print(f"O valor 9 apareceu {numero.count(9)} vezes")
if 3 in numero:
    print(f"O valor 3 apareceu {numero.index(3)+1} posição")
else:
    print('O Valor 3 não foi digitado em nenhuma posição')
print('Os valores digitados, PARES foram: ', end=' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=" ")
