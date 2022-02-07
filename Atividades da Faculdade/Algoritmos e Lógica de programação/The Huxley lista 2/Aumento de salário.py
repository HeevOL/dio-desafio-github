salario = float(input())
if salario <= 280.0:
    salario = salario + salario * 0.2
elif salario <= 700.0:
    salario = salario + salario * 0.15
elif salario <= 1500.0:
    salario = salario + salario * 0.1
else:
    salario = salario + salario * 0.05
print(salario)