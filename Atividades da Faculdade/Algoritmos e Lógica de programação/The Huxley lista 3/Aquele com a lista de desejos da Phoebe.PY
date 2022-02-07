fazeres = int(input())

listafazer = []
for i in range(fazeres):
    f = input()
    listafazer.append(f)

feitos = int(input())

listafeito = []
for c in range(feitos):
    k = input()
    listafeito.append(k)

cont = fazeres
listasobra = []
for x in range(len(listafazer)):
    listasobra.append(listafazer[x])

for x in range(len(listafeito)):
    for y in range(len(listafazer)):
        if listafeito[x] == listafazer[y]:
            cont = cont - 1
            item = listafeito[x]
            listasobra.remove(item)

if cont == 0:
    print('Smelly Cat, Smelly Cat, what are they feeding you?')
else:
    print('Ainda falta(m)', cont, 'objetivo(s)!')
    for j in range(cont):
        print(listasobra[j])
