def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)
# Programa Principal
soma(4, 5)

def contador(*num):
    tam = len(num)
    print(f'Recebi o valor {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8,0)
contador(4, 4, 7, 6, 2)
