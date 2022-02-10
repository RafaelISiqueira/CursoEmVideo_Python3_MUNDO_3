#Ler nome do jogador, quantas partidas jogou e quantos gols ele fez,
#Mostrar o saldo de gols, e quantos gols por partida:

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))
for c in range(0, tot):
    partidas.append(int(input(f'   Quantos gols na partida {c}?  ')))
jogador['gols'] = partidas [:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} Partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols. ')
