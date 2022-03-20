#Faça um Boletim com uma lista composta, que possa ser consultada o valor das notas
#Cadastrar aluno, calcular a média, e mostrar as notas selecionando seus Numeros

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = int(input('Nota PROVA - 1: '))
    nota2 = int(input('Nota PROVA - 2: '))
    media = (nota1+nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resposta = str(input("Quer continuar: [S/N] "))
    if resposta in 'Nn':
        break
print('-='*30)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno: (999 interrompe): '))
    if opc == 999:
        print('FINALIZADO')
        break
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} São {ficha[opc][1]}')
    print('<<< VOLTE SEMPRE >>>')