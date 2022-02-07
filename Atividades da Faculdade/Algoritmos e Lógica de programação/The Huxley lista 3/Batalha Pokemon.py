import math
batalhas = int(input())

for i in range(batalhas):

    vClodes, vBezaliel, dClodes, dBezaliel = input().split()
    vClodes = int(vClodes)
    vBezaliel = int(vBezaliel)
    dClodes = int(dClodes)
    dBezaliel = int(dBezaliel)
    vencedor = ''

    while vencedor == '':
        rParaClodes = math.ceil(vBezaliel / dClodes)
        rParaBezaliel = math.ceil(vClodes / dBezaliel)
        if rParaClodes >= rParaBezaliel:
            dClodes = dClodes + 50
        else:
            vBezaliel = vBezaliel - dClodes
        vClodes = vClodes - dBezaliel
        if vBezaliel <= 0:
            vencedor = 'Clodes'
        elif vClodes <= 0:
            vencedor = 'Bezaliel'
    print(vencedor)

    ''''if d1 < d2:
            d1 = d1 + 50
        else:
            v2 = v2 - d1
        v1 = v1 - d2
        if v2 <= 0:
            vencedor = 'Clodes'
        elif v1 <= 0:
            vencedor = 'Bezaliel
            '''''
