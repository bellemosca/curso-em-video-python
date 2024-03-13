primeira = float(input("Primeira nota: "))
segunda = float(input("Segunda nota: "))

media = (primeira + segunda) / 2

if media < 5.0:
    print(f"Sua média foi de {media:.1f}. Você está REPROVADO!")
elif media >= 5.0 and media <= 6.9:
    print(f"Sua média foi de {media:.1f}. Você está de RECUPERAÇÃO!")
elif media >= 7.0:
    print(f"Sua média foi de {media:.1f}. Você está APROVADO!")
