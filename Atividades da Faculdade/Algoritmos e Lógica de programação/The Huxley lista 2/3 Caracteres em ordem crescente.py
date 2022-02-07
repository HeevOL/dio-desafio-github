l1 = input().split()
c1 = str(l1[0])
c2 = str(l1[1])
c3 = str(l1[2]) 
l2 = input().split()
c4 = str(l2[0])
c5 = str(l2[1])
c6 = str(l2[2])

if c1 <= c2 and c2 <= c3:
    print(c1, c2, c3)
elif c1 <= c3 and c3 <= c2:
    print(c1, c3, c2)
elif c2 <= c1 and c1 <= c3:
    print(c2, c1, c3)
elif c2 <= c3 and c3 <= c1:
    print(c2, c3, c1)
elif c3 <= c1 and c1 <= c2:
    print(c3, c1, c2)
elif c3 <= c2 and c2 <= c1:
    print(c3, c2, c1)

if c4 <= c5 and c5 <= c6:
    print(c4, c5, c6)
elif c4 <= c6 and c6 <= c5:
    print(c4, c6, c5)
elif c5 <= c4 and c4 <= c6:
    print(c5, c4, c6)
elif c5 <= c6 and c6 <= c4:
    print(c5, c6, c4)
elif c6 <= c4 and c4 <= c5:
    print(c6, c4, c5)
elif c6 <= c5 and c5 <= c4:
    print(c6, c5, c4)