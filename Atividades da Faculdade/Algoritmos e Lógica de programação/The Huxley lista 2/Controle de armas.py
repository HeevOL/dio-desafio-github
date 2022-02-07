nacionalidade = str(input())
ocupacao = str(input())
quantDeArmas = int(input())
calibre = int(input())

if quantDeArmas == 0:
    print("Liberado")
elif nacionalidade == "E" and quantDeArmas != 0:
    print("Barrado")
elif nacionalidade == "B" and ocupacao == "M":
    print("Liberado")
elif nacionalidade == "B" and ocupacao == "T" or ocupacao == "O" and quantDeArmas == 1 and calibre <= 22:
    print("Liberado")
elif nacionalidade == "B" and ocupacao == "C" and quantDeArmas == 2 and calibre <= 38:
    print("Liberado")
else:
    print("Barrado")
