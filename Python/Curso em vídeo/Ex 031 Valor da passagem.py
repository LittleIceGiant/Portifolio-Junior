""" Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas. """

distanciaTotal = float(input("Quantos Km a viagem terá? "))
if distanciaTotal <= 200:
    valor = distanciaTotal * 0.50
else:
    valor = distanciaTotal * 0.45
print(f"O valor da passagem será de R$ {valor:.2f} reais")
