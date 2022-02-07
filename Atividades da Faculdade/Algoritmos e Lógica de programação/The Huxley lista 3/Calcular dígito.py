chave = input()
while chave != 'FIM':   
    d1 = int(max(chave[0:3]))
    d2 = int(max(chave[4:7]))
    d3 = int(max(chave[8:11]))
    verificador = int(chave[12])
    soma = d1+d2+d3
    if soma % 10 == verificador:
        print("VALIDO")
    else:
        print("INVALIDO")
    chave = input()
