l = input().split()
D = int(l[0]) #Distancia da viagem
R = int(l[1]) #Reais disponiveis para gastar com gasolina caso necessario.
L = int(l[2]) #Capacidade em litros do tanque do carro. E na questão diz q o carro faz 10KM/L
P = int(l[3]) #Numeros de postos de gasolina no percurso.
G = int(l[4]) #Valor da gasolina.
#Todos os valores acima são inteiros e > 0
if L * 10 * P < D/(P+1): #Verifica se o tanque tem capacidade para rodar o carro até o posto mais proximo.
    print("Nao pode viajar.")
elif D/10 <= L: #Verifica se a capacidade do tanque é maior ou igual do que a propria distancia, caso seja, nem será preciso parar em um posto.
    print("Pode viajar.")
    print(f"R$: {R:.0f}")
elif D/10 > L and P >= 1: #Calcula se o valor disponivel é suficiente para fazer a viagem.
    reabastecer = (D/10 - L) * G
    saldo = R - reabastecer
    if saldo >= 0:
        print("Pode viajar.")
        print(f"R$: {saldo:.0f}")
    else:
        print("Nao pode viajar.")
