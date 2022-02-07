ima = int(input())
lista1 = []
for i in range(ima):
    lista1.append(input())

lista2 = []
for i in range(ima):
    d = lista1[i]
    lista2.append(d[0])
lista2.append('')

cont = 1
maior = 0
grupos = 0
for i in range(ima):
    if lista2[i] == lista2[i+1]:
        cont = cont + 1
    else:
        grupos = grupos + 1
        if cont > maior:
            maior = cont
            cont = 1
        else:
            cont = 1
print(f'groups: {grupos}, biggest: {maior}')
