sexo = str(input())
tempoDeCasa = int(input())
salario = float(input())
if sexo == "h" and tempoDeCasa > 15:
    salario = salario + (salario * 0.2)
elif sexo == "m" and tempoDeCasa > 10:
    salario = salario + (salario * 0.25)
else:
    salario = salario + 200.0
print("%.2f" % salario)
