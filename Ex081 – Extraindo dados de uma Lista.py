#extraindo dados de uma lista,
#Quantos números foram digitados,
#decrescente,
#e mostrar se tem ou não 5.

valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resposta = str(input("Quer continuar? [S/N] "))
    if resposta in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print('o Valor 5 faz parte da lista! ')
else:
    print('O valor 5 não foi encontrado na lista! ')
