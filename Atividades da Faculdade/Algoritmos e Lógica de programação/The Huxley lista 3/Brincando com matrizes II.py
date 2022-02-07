matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        n = int(input())
        matriz[i].append(n)

soma = 0 
qtn = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > 0:
            soma += matriz[i][j]
            qtn += 1 
media = soma/qtn

menor = 9999999999999
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] < menor:
            menor = matriz[i][j]

if menor % 2 == 0:
    delta = 1
else:
    delta = 0

soma_nao_diagonal = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i != j:
            soma_nao_diagonal += matriz[i][j]

print(f'{media:.2f} {menor} {delta} {soma_nao_diagonal}')