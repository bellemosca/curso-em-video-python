primeiro = int(input("Digite o primeiro valor: "))
segundo = int(input("Digite o segundo valor: "))

# maior = max(primeiro, segundo)

if primeiro > segundo:
    print(f"{primeiro} é maior que {segundo}")
elif primeiro < segundo:
    print(f"{segundo} é maior que {primeiro}")
else:
    print("Eles são iguais")
