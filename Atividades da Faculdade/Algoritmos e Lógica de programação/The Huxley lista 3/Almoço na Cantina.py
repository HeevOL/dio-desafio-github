comida = str.lower(input())
bebida = str.lower(input())
lasanha = 8.0
estrogonofe = 11.0
refrigerante = 3.0
suco = 2.5
total = 0
if comida == 'lasanha':
    total = lasanha + total
elif comida == 'estrogonofe':
    total = estrogonofe + total
if bebida == 'refrigerante':
    total = total + refrigerante
elif bebida == 'suco':
    total = total + suco

print('%.2f' %total)
