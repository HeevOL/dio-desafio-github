portugues = True
c = 0
while portugues >= 0:
    portugues = int(input())
    if portugues >= 0:       
        matematica = int(input())
        redacao = float(input())
        if portugues / 50 >= 0.8 and matematica / 35 >= 0.6 and redacao >= 7:
            c += 1
print(c)    