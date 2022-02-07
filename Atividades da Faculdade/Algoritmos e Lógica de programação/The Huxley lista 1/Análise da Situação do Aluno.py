x = input().split()
nota = float(x[0])
a = int(x[1])
f = int(x[2])
freq = (f * 100) / a
if (nota >= 5 and freq <= 25) or (nota >= 7 and freq <= 50):
    print("APROVADO")
else:
    print("REPROVADO")
