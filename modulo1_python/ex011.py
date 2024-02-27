largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
tinta = area / 2

print(
    f"Sua parede tem dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.2f}"
)
print(f"Para pintar essa parede, você precisará de {tinta:.2f}L de tinta")
