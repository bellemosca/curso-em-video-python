print("ANALISADOR DE TRIÂNGULOS")
print("-=" * 20)
a = float(input("Primeiro seguimentos: "))
b = float(input("Segundo seguimento: "))
c = float(input("Terceiro seguimento: "))

if a < b + c and b < a + c and c < a + b:
    print("Pode formar um triângulo.")
else:
    print("Não é possível formar um triângulo.")
