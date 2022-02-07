l = input().split()
Cv = int(l[0])
Ce = int(l[1])
Cs = int(l[2])
Fv = int(l[3])
Fe = int(l[4])
Fs = int(l[5])
pontosC = Cv * 3 + Ce
pontosF = Fv * 3 + Fe
if pontosC > pontosF:
    print("C")
elif pontosC < pontosF:
    print("F")
elif pontosF == pontosC and Cs > Fs:
    print("C")
elif pontosC == pontosF and Cs < Fs:
    print("F")
else:
    print("=")
