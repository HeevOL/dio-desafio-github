level = int(input())
if level >= 1 and level <= 20:
    print("Potencia de :", (20 + (level ** 3)), "W")
elif level >= 21 and level <= 40:
    print("Potencia de :", (8000 + (level - 10) ** 2), "W")
elif level >= 41 and level <= 60:
    print("Potencia de :", 9000 + (5 * level), "W")
elif level >= 61 and level <= 80:
    print("Potencia de :", 9300 + (2 * level), "W")
else:
    print("Potencia de :", 9500 + level, "W")
