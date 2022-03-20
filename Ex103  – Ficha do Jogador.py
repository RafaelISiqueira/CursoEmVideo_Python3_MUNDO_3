# Digitar nome do Jogador e número de gols usando def

def ficha(jogador='<desconhecido>', gol=0):  # Caso esteja vazio
    print(f'O jogador {jogador} fez {gol} gols(s) no campeonato.')


# Principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
