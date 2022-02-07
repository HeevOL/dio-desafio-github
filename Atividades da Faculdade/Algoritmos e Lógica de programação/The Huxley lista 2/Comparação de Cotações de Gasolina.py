gEUA = float(input())
lBrasil = float(input())
cotacao = float(input())
valorGEUA = gEUA * cotacao / 3.8
print("Gasolina EUA: R$" "%.2f" % valorGEUA)
print("Gasolina Brasil: R$" "%.2f" % lBrasil)
if valorGEUA < lBrasil:
    print("Mais barata nos EUA")
elif valorGEUA > lBrasil:
    print("Mais barata no Brasil")
else:
    print("Igual")
print(valorGEUA)
print(lBrasil)
