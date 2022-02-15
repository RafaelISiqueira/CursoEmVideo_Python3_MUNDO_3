from Ex115.Lib.interface import *


# Se o Arquivo existe
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# Criar um Arquivo caso nãoo exista
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #+ cria o Arquivo caso não exista
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} Criado com sucesso!')


# Ler o Arquivo existente ou criado
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos.')
        #print(a.readlines()) #Pega linhas e transforma em Listas.
        #print(a.read()) #Deixa em ordem do arquivo.
    finally:
        a.close()


# Cadastrar novas pessoas
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # "a" é para colocar arquivos de "t" texto
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
