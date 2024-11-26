""" Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. """
from random import randrange
usuario = int(input("Digite um número de 0 à 10: "))
computer = randrange(0, 10)
cont = 1
while usuario != computer:
    usuario = int(input("Não foi dessa vez, tente novamente: "))
    cont += 1
    computer = randrange(0, 10)
if cont <= 5:
    print(f'Você acertou! Eu "pensei" em {computer} e você adivinhou! Você foi bem rápido!')
else:
    print(F'Você FINALMENTE acertou! Eu "pensei" no número {computer}, assim como você. Você precisou de {cont} tentativas para conseguir.')