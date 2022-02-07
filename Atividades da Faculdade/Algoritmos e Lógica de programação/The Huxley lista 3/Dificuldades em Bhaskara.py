import math
n = int(input())
lista = []

for i in range(n):
    lista.append(input())

for i in range(1,n+1):
    equacao = lista[i-1]
    A, B, C = equacao.split(" + ")
    C = float(C)
    B = float(B[:(len(B)-1)])
    A = float(A[:(len(A)-3)])
    delta = B**2 - 4 * A * C
    print(f'Test {i}: {lista[i-1]}')
    
    if delta < 0:
        print('SEM RESPOSTA\n')

    elif delta == 0:
        X1 = (-B + math.sqrt(delta))/(2*A)
        X2 = (-B - math.sqrt(delta))/(2*A)
        print(f'X = {X1:.2f}\n')

    else:
        X1 = (-B + math.sqrt(delta))/(2*A)
        X2 = (-B - math.sqrt(delta))/(2*A)
        print(f'X1 = {X1:.2f}')
        print(f'X2 = {X2:.2f}\n')
    