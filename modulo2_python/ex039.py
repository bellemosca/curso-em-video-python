from datetime import datetime

sexo = str(input("Qual seu sexo? M/F ")).upper()
ano = int(input("Ano de nascimento: "))

ano_atual = datetime.now().year
alistamento = ano + 18
idade = ano_atual - ano

print(f"Quem nasceu em {ano} tem {idade} em {ano_atual}")

if sexo.startswith("M"):
    if idade > 18:
        print(f"Você já deveria ter se alistado há {ano_atual - alistamento} anos.")
        print(f"Seu alistamento foi em {alistamento}")
    elif idade < 18:
        print(f"Faltam {18 - idade} anos para o seu alistamento.")
        print(f"Seu alistamento será em {alistamento}.")
    elif idade == 18:
        print(f"Esta no ano de você se alistar.")
else:
    print("Você não precisa se alistar.")
