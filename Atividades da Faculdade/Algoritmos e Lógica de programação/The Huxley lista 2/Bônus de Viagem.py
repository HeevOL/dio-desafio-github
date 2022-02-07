salario = float(input())
bonus = salario * 0.75
if bonus < 2000:
    print("ARGENTINA")
elif bonus >= 2000 and bonus <= 3000:
    print("ESPANHA")
else:
    print("ALEMANHA")
    