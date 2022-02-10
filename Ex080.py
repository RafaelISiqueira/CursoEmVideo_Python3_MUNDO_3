#Lista ordenada sem repetições e em ordem:

lista = []
for c in range(0, 5):
    n = int(input("Digite um número: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-='*30)
print(f'Os números digitados em ordem foram: {lista}')