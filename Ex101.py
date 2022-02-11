#colocar sua idade, e dizer se pode votar, não pode, ou é opcional:

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 16:
        return f'Com {idade} anos: NÂO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

#Principal
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
