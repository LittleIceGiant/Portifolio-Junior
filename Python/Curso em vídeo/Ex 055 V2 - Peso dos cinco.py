"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input(f"Digite o pessoa nº{i}: "))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f"O menor peso é: {menor}")
print(f"O maior peso é: {maior}")