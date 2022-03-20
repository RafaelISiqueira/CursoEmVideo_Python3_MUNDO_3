#crie um código onde mostre a palavra e mostre quais suas vogais:

palavras = ('aprender',
            'programar',
            'linguagem',
            'python',
            'curso',
            'grátis',
            'estudar',
            'praticar',
            'trabalhar',
            'mercado',
            'programador',
            'futuro')

for p in palavras:
    print(f"\nNa palavra {p} temos: =--> ", end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
