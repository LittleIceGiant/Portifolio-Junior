""" Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o."""
listaNumerica = []
tuplaNomes = ("primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto")
soma = 0
for i in range(0, 6):
    variavelDeTransito = int(input(f"Digite o {tuplaNomes[i]} número: "))
    listaNumerica.append(variavelDeTransito)
for i in listaNumerica:
    if i % 2 == 0:
        soma += i
print(f"Total da soma apenas dos números pares: {soma}")
