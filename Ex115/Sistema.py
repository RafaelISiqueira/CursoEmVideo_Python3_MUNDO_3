from Ex115.Lib.interface import *
from Ex115.Lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastros', 'New Cadastros', 'Sair do Sistema'])

    # Lista do Conteúdo de Arquivo!
    if resposta == 1:
        lerArquivo(arq)

    # Criar novo cadastro!
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    # sair do programa
    elif resposta == 3:
        cabeçalho('Saindo do Programa...')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

