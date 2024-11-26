""" Melhore o DESAFIO 61, perguntando para o usuário se ela quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar zero termos. """
from time import sleep

questao = 1
repete = 10
contador = 0
adicinal = 0
termo = float(input("Digite o termo: "))
razao = float(input("Digite a razão: "))
while questao != 0:
    while contador != repete:
        termo += razao
        contador += 1
        print(f"\033[34m{contador}º Termo: {termo:.0f}\033[m", end="")
        print(" // " if contador != repete else "", end="")
    if contador == repete:
        questao = int(input("\nQuantos termos a mais você quer mostrar? Digite \033[31m0\033[m caso queira encerrar: "))
        repete += questao
    if questao == 0:
        print("Programa encerrado")
