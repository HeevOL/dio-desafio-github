matriz = [[],[],[]]
for i in range(3):
    for j in range(3):
        n = int(input())
        matriz[i].append(n)

soma = 0 
qtn = 0
for i in range(len(matriz)):
    soma += sum(matriz[i])
    qtn += len(matriz[i])  
media = soma/qtn

maior = -9999999999999
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] > maior:
            maior = matriz[i][j]

if maior > 0:
    delta = 1
elif maior < 0:
    delta = -1
else:
    delta = 0

soma_diagonal = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            soma_diagonal += matriz[i][j]

print(f'{media:.2f} {maior} {delta} {soma_diagonal}')