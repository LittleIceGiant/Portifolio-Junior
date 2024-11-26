""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares. """

contValNove = 0
valueOne = float(input("Digite o primeiro valor: "))
if valueOne == 9:
    contValNove += 1
valueTwo = float(input("Digite o segundo valor; "))
if valueTwo == 9:
    contValNove += 1
valueThree = float(input("Digite o terceiro valor: "))
if valueThree == 9:
    contValNove += 1
valueFour = float(input("Digite o quarto valor: "))
if valueFour == 9:
    contValNove += 1
addedValues = (valueOne, valueTwo, valueThree, valueFour)

print(contValNove)