n, e = input().split()
n = int(n)
e = int(e)

g = input().split()
lista = []
lista.extend(g)

listainteira = []
for i in range(len(lista)):
    listainteira.append(int(lista[i]))

cond = False
for x in range(n):
    for y in range(n):
        if x != y:
            if listainteira[x] + listainteira[y] == e:
                cond = True
                break

if cond == True:
    print('SIM')
else:
    print('NAO')           
