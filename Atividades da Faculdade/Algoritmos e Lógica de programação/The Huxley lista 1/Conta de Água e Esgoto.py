x = input().split()
q = float(x[0])
v = float(x[1])
print("%.2f" % (q*1000*v))
print("%.2f" % ((q*1000*v)*0.8))
print("%.2f" % (((q*1000*v)*0.8)+(q*1000*v)))
