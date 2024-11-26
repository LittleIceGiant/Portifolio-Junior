""" Ex 023 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígios separado

Ex: Digite um número: 1834
Unidade: 4
dezena: 3
centenha: 8
milhar: 1
 """

entradaDeNumero = str(input("Digite um número inteiro de 0 à 9999: "))
entradaDeNumero.split()
print(f"Unidade: {entradaDeNumero[3]} \nDezena: {entradaDeNumero[2]} \nCentena: {entradaDeNumero[1]} \nMilhar: {entradaDeNumero[0]}")
