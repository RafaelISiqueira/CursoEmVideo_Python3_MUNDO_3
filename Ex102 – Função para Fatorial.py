#Usar uma função fatorial, usar o Show(que mostra ou não o calculo) e o help para ver o comentario.
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O numero a ser calculado
    :param show: mostrar ou não mostrar (opcinal)
    :return: O valor do Fatorial de um número N.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#PRINCIPAL
print(fatorial(17, show=True))
#help(fatorial)