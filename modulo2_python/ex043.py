peso = float(input("Qual o seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.1f}. Você está ABAIXO DO PESO.")
elif imc > 18.5 and imc < 25:
    print(f"Seu IMC é {imc:.1f}. Você está com PESO IDEAL.")
elif imc > 25 and imc < 30:
    print(f"Seu IMC é {imc:.1f}. Você está com SOBREPESO.")
elif imc > 30 and imc < 40:
    print(f"Seu IMC é {imc:.1f}. Você está com OBESIDADE.")
elif imc > 40:
    print(f"Seu IMC é {imc:.1f}. Você está com OBESIDADE MÓRBIDA.")
