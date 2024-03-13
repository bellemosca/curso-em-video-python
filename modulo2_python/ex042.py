print("ANALISADOR DE TRIÂNGULOS")
print("-=" * 20)
a = float(input("Primeiro seguimentos: "))
b = float(input("Segundo seguimento: "))
c = float(input("Terceiro seguimento: "))

if a < b + c and b < a + c and c < a + b:
    print("Pode formar um triângulo.")
    if a == b == c:
        print("Esse triângulo é EQUILÁTERO.")
    elif a == b or b == c or a == c:
        print("Esse triângulo é ISÓSCELES.")
    elif a != b != c:
        print("Esse triângulo é ESCALENO.")
else:
    print("Não é possível formar um triângulo.")
