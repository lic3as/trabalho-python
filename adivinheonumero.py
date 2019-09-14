import random

jogadaComputador = random.randrange(0,100)
print("Adivinhe o numero que estou pensando:")
jogadaPlayer = input("SUA JOGADA:")

aux = 1
while aux  jogadaComputador

    print("Player:", jogadaPlayer)

        if jogadaPlayer == jogadaComputador:
            print("Voce acertou!!!")
        else jogadaPlayer > jogadaComputador:
            print("Seu numero e maior")
        else jogadaPlayer < jogadaComputador:
            print("Seu numero e menor")

        aux += 1

if (jogadaPlayer == jogadaComputador):
    print("Voce acertou!!!")




