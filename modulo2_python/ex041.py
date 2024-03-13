from datetime import datetime

anoNascimento = int(input("Ano do nascimento: "))

idade = datetime.now().year - anoNascimento

if idade <= 9:
    print(f"Você tem {idade}, então sua categoria é MIRIM.")
elif idade <= 14:
    print(f"Você tem {idade}, então sua categoria é INFANTIL.")
elif idade <= 19:
    print(f"Você tem {idade}, então sua categoria é JUNIOR.")
elif idade <= 25:
    print(f"Você tem {idade}, então sua categoria é SÊNIOR.")
elif idade > 25:
    print(f"Você tem {idade}, então sua categoria é MASTER.")
