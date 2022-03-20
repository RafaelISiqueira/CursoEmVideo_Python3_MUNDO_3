def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if formato is False else Moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else Moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else Moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else Moeda(res)


def Moeda(preço=0, Moeda="R$"):
    return f'{Moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-='*15)
    print('Resumo Do Valor'. center(30))
    print('-='*15)
    print(f'Preço Analisado: \t{Moeda(preço)}')
    print(f'Dobro do Preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}')
    print('-='*15)
