print("----------LOJA DA BELLE----------")
compras = float(input("Preço das compras: R$"))
print("---FORMAS DE PAGAMENTO---")
print("[ 1 ] à vista dinhiero/pix")
print("[ 2 ] à vista cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")
opcao = int(input("Qual é a opção? "))

if opcao == 1:
    total = compras * 0.90
elif opcao == 2:
    total = compras * 0.95
elif opcao == 3:
    total = compras
    parcelas = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcelas:.2f}.")
elif opcao == 4:
    total = compras * 1.20
    totalParcelas = int(input("Quantas parcelas? "))
    parcela = total / totalParcelas
    print(
        f"Sua compra será parcelada em {totalParcelas}x de R${parcela:.2f} com juros."
    )
else:
    total = compras
    print("Opção inválida de pagamento. Tente novamente")

print(f"Sua compra de R${compras} vai custar R${total} no final.")
