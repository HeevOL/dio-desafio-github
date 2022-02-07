v = int(input())
h, m, s = 0, 0, 0
while v != 0:
    if v >= 3600:
        h = (h + 1)
        v = v - 3600
    elif v >= 60:
        m = m+1
        v = v - 60
    else:
        s = v
        v = 0
print(h, "h", m, "m", s, "s")
