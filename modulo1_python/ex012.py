preco = float(input("Qual é o preço do produto? R$"))
desconto = preco * (1 - 0.05)
print(
    f"O valor do produto que custava R${preco}, na promoção com desconto de 5% vai custar R${desconto:.2f}"
)
