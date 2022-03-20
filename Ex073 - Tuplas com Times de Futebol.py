#Mostrar tabela do brasileirão com todos os times,
#Com os 5 primeiros,
#4 ultimos,
#Ordem alfabetica,
#Posição do chapecoence.
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
         'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo',
         'Fluminence', 'Sport Recife', 'EC Vítoria', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-='*15)
print(f'Lista de times do brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros times do Brasileirão:{times[0:5]}')
print('-='*15)
print(f'Os 4 ultimos colocados são: {times[-4:]}')
print('-='*15)
print(f'Os times em ordem ALFABETICA: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição')
