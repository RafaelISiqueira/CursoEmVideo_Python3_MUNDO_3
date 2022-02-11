# Criar uma Função nota, que pode receber varios alunos,
# Quantidade de provas,
# Maior nota,
# Menor nota,
# Media,
# Situação.

def notas(*n, sit=False):
    """
    -->Função para analiasr notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos
    :param sit:valor opcional
    :return:
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#PRINCIPAL
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
#help(notas)
