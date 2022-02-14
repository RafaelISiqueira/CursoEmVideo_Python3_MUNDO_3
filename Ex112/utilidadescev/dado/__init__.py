def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha():
            print(f'\033[0;31mERRO \"{entrada}\" é um preço INVÁLIDO!\033[m')
        else:
            valido = True
            return float(entrada)
