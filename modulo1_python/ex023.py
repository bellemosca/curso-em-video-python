numero = int(input("Informe um número: "))
u = numero // 1 % 10
c = numero // 10 % 10
d = numero // 100 % 10
m = numero // 1000 % 10

print(f"Analisando o número {numero}")
print(f"Unidade: {u}")
print(f"Centena: {c}")
print(f"Dezena: {d}")
print(f"Milhar: {m}")
