velocidade = float(input("Qual a velocidade atual do carro? "))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print("MULTADO!Você excedeu o limete de 80km/h!")
    print(f"Você deve pagar uma multa de R${multa}!")
else:
    print("Você está dentro da velocidade permitida.")

print("Tenha um bom dia! Dirija com segurança!")
