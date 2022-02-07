lista = input().split()
v1 = int(lista[0])
v2 = int(lista[1])
v3 = int(lista[2])
if v1 == 1:
    print(v1, "GALÃO ->", "%.2f" % (v1*3.7854), "LITROS")
else:
    print(v1, "GALÕES ->", "%.2f" % (v1*3.7854), "LITROS")
if v2 == 1:
    print(v2, "GALÃO ->", "%.2f" % (v2*3.7854), "LITROS")
else:
    print(v2, "GALÕES ->", "%.2f" % (v2*3.7854), "LITROS")
if v3 == 1:
    print(v3, "GALÃO ->", "%.2f" % (v3*3.7854), "LITROS")
else:
    print(v3, "GALÕES ->", "%.2f" % (v3*3.7854), "LITROS")
