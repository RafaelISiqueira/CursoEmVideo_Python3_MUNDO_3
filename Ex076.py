#Criar uma lista de materiais, seus preços, e organizar em forma de tabela:
Lista = ('Lapis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 20.30,
         'Livro', 34.90)
print('-'*34)
print(f'{"LISTAGEM DE PREÇOS":^34}')
print('-'*34)
for pos in range(0, len(Lista)):
    if pos % 2 == 0:
        print(f'{Lista[pos]:.<23}', end=" ")
    else:
        print(f'R${Lista[pos]:>8.2f}')
print('-'*34)