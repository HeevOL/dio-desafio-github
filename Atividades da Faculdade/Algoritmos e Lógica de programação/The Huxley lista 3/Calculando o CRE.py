semestre = 1
CRE = 0
contCH = 0
contNota = 0
situacao = ""
while (semestre > 0) and (semestre <= 10):

    semestre = int(input())

    if (semestre > 0) and (semestre <= 10):
        cargaHoraria = int(input())
        nota = int(input())
        situacao = str(input())

        if (situacao == "A" or situacao == "R" or situacao == "RF") and (cargaHoraria == 33 or cargaHoraria == 50 or
                                                                         cargaHoraria == 67 or cargaHoraria == 83):
            contNota = contNota + (nota * cargaHoraria)
            contCH = contCH + cargaHoraria
            CRE = contNota/contCH

if CRE > 0:
    print("%.2f" % CRE)
else:
    print("entrada invalida")
