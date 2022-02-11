#use Função para calcular Área base x Altura.

def area(largura,comprimento):
    a = largura * comprimento
    print(f'A Área de terreno {largura} x {comprimento} é de {a}m².')


# Programa Principal
print(' Controle de Terrenos')
print('-'*20)
l = float(input('largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
