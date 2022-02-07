medidaTemperatura = str(input())
valorTemperatura = float(input())
if (medidaTemperatura == "C" and valorTemperatura < -273.0) or (medidaTemperatura == "F" and valorTemperatura < -459.67) or (medidaTemperatura == "K" and valorTemperatura < 0):
    print("Valor de temperatura abaixo do minimo")
elif medidaTemperatura == "C":
    F = (valorTemperatura * 9/5) + 32
    K = valorTemperatura + 273.15
    print("{:.2f} F".format(F))
    print("{:.2f} K".format(K))
elif medidaTemperatura == "F":
    C = (valorTemperatura - 32) * 5/9
    K = (valorTemperatura - 32) * 5/9 + 273.15
    print("{:.2f} C".format(C))
    print("{:.2f} K".format(K))
elif medidaTemperatura == "K":
    C = valorTemperatura - 273.15
    F = (valorTemperatura - 273.15) * 9/5 + 32 
    print("{:.2f} C".format(C))
    print("{:.2f} F".format(F))
