dias_alugado = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quantos Km rodados? "))

diaria = 60 * dias_alugado
total_km = 0.15 * km_rodados
total_pago = diaria + total_km

print(f"O total a pagar é de R${total_pago:.2f}")
