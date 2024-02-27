import random
import time

#
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
jogador = int(input("Em que número eu pensei?"))
computador = random.randint(0, 5)
#
print("PROCESSANDO...")
time.sleep(3)
#
if jogador == computador:
    print("Parbéns! Você venceu.")
else:
    print(f"Ganhei!Eu pensei no número {computador} e não no {jogador}.")
