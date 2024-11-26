""" Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu. """
from random import randrange
from time import sleep
aleatorio = randrange(0, 6)
UNumero = int(input("Eu estou pensando em um número de 0 à 5, vamos ver se você consegue adivinhar qual é: "))
print("PROCESSANDO...")
sleep(1)
if UNumero > 5:
    input(f"O número precisava ser entre 0 e 5, lembra?")
else:
    if UNumero == aleatorio:
        print(f"Olha só, você acertou! O número que eu pensei foi mesmo o {aleatorio}!")
    else:
        print(f"Você errou. O número em que pensei foi o {aleatorio}")