salario = float(input("Qual o salário do funcionário? R$"))
aumento = salario * (1 + 0.15)
print(
    f"Um funcionário que ganhava R${salario:.2f}, com aumento de 15%, passa a receber R${aumento:.2f}"
)
