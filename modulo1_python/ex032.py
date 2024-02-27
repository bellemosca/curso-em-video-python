import datetime

ano = int(input("Qual ano quer analizar? Coloque 0 para analizar o ano atual: "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
    print("Esse ano é Bissexto.")
else:
    print("Esse ano não é Bissexto.")
