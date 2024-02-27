# distância da viagem
distancia = float(input("Qual é a distância da sua viagem? "))
# 0.50 até 200km e 0.45 para viagens mais longas
if distancia <= 200:
    custo = distancia * 0.5
    print(f"Você está prestes a começar uma viagem de {distancia}Km")
    print(f"O preço da sua passagem será de R${custo:.2f}")
else:
    custo = distancia * 0.45
    print(f"Você está prestes a começar uma viagem de {distancia}Km")
    print(f"O preço da sua passagem será de R${custo:.2f}")
