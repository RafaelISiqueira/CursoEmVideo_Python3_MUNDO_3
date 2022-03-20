#Use função para mostrar um texto com o parametro com tamanho adaptável.
def escreva(msg):
    tam = len(msg) + 4
    print('+' * tam)
    print(f' {msg}')
    print('+' * tam)


# Programa principal
escreva('Rafael Luiz Siqueira')
escreva('Curso de Python no Youtube')
escreva('VAMO DALE')
