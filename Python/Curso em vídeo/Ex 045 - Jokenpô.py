"""Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
jajanken = ("Pedra", "Papel", "Tesoura")
escolha = randint(0, 2)
jokenpo = int(input("1 - Pedra\n2 - Papel\n3 - Tezoura\nSelecione sua mão: "))
print(f"Computador: {jajanken[escolha]}\nVoce: {jajanken[jokenpo - 1]}")
