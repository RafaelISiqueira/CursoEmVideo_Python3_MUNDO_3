num = [2, 7, 9, 1] #lista mutavel
num[2] = 3 #Mudar um Numero
num.append(7) #adiconar um número
num.sort(reverse=True) # sort ordem alfabetica. reverse True decrescente
num.insert(2,0) # add 4 na posição 2
num.pop(0) #pop elimina da lista
if 5 in num:
    num.remove(5)
else:
    print('Não achei o numero 5 :( ')
print(num)
print(f'Essa lista tem {len(num)} Elementos. ')
