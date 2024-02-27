import math

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
# h = (oposto ** 2 + adjacente ** 2) ** 1/2
h = math.hypot(oposto, adjacente)
print(f"O comprimento da hipotenusa é {h:.2f}")
