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