salario = float(input("Qual o salário do funcionário? R$"))
# aumento de 10% para salário acima de 1250 e de 15% para menores que isso.
if salario > 1250:
    aumento = salario * 1.10
    print(f"Quem ganhava R${salario} passa a ganhar R${aumento:.2f}")
else:
    aumento = salario * 1.15
    print(f"Quem ganhava R${salario} passa a ganhar R${aumento:.2f}")
