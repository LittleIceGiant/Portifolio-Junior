""" Melhore o DESAFIO 61, perguntando para o usuário se ela quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar zero termos. """
from time import sleep

questao = 1
repete = 0
contador = 0
mais = 4
termo = float(input("Digite o termo: "))
razao = float(input("Digite a razão: "))
while mais != 0:
    repete += mais
    while contador != repete:
        print(f"{contador}º termo: {termo}")
        contador += 1