nome = str(input("Digite seu nome completo:")).strip()

print(f"Seu nome em maiúsculo é {nome.upper()}")
print(f"Seu nome em minúsculo é {nome.lower()}")
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
separa = nome.split()
print(f"Seu primerio nome é {separa[0]} e tem {len(separa[0])} letras")
