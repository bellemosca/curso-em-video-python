numero = int(input("Digite um número: "))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print(c, end=" ")

print(f"O número {numero} foi divisível {tot}", end=" ")
if tot == 2:
    print("E por isso ele é primo.")
else:
    print("E por isso ele não é primo.")
