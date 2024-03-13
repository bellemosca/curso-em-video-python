import random

itens = ["Pedra", "Papel", "Tesoura"]
computador = random.choice(itens)
print("Suas opções:")
print("[ 0 ] PEDRA")
print("[ 1 ] PAPEL")
print("[ 2 ] TESOURA")
jogador = int(input("Qual é a sua jogada? "))
print(f"Computador jogou {computador}")
print(f"Jogador jogou {jogador}")

if computador == 0:
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA.")
elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATE!")
    elif jogador == 2:
        print("JOGADOR VENCE!")
    else:
        print("JOGADA INVÁLIDA.")
elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATE!")
    else:
        print("JOGADA INVÁLIDA.")
