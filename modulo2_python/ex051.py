primeiroTermo = int(input("Primeiro Termo: "))
razao = int(input("Razão: "))
decimo = primeiroTermo + (10 - 1) * razao
for c in range(primeiroTermo, decimo + razao, razao):
    print(f"{c}", end=" -> ")
print("ACABOU.")
