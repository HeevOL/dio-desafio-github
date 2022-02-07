D1 = int(input())
l1 = input().split()
CO = float(l1[0])
RE = float(l1[1])
DE = float(l1[2])
D2 = int(input())
l2 = input().split()
CO2 = float(l2[0])
RE2 = float(l2[1])
CE = float(l2[2])
DE2 = float(l2[3])
if D1 < 20:
    N = CO + (RE*0.9) + (DE*0.85)
elif D1 == 20:
    N = (CO*0.88) + (RE*0.85) + (DE*0.8)
elif D1 == 21:
    N = (CO*0.83) + (RE*0.78) + (DE*0.73)
elif D1 == 22:
    N = (CO*0.8) + (RE*0.78) + (DE*0.7)
elif D1 == 23:
    N = (CO*0.75) + (RE*0.71) + (DE*0.65)
elif D1 == 24:
    N = (CO*0.65) + (RE*0.65) + (DE*0.5)

if D2 == 25:
    A = (CO2*0.85) + (RE2*0.87) + (CE) + (DE2*0.9)
elif D2 == 26:
    A = (CO2*0.81) + (RE2*0.75) + (CE*0.95) + (DE2*0.77)
elif D2 == 27:
    A = (CO2*0.76) + (RE2*0.7) + (CE*0.88) + (DE2*0.67)
elif D2 == 28:
    A = (CO2*0.7) + (RE2*0.68) + (CE*0.8) + (DE2*0.65)
elif D2 == 29 or D2 == 30:
    A = (CO2*0.65) + (RE2*0.6) + (CE*0.67) + (DE2*0.58)
elif D2 == 31:
    A = (CO2*0.6) + (RE2*0.53) + (CE*0.55) + (DE2*0.34)

T = N + A

print(f"Compras de natal: R$ {N:.2f}.")
print(f"Compras de ano novo: R$ {A:.2f}.")
print(f"Total das compras: R$ {T:.2f}.")
