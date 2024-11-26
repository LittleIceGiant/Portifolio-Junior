""" Faça um programa que leia um ano qualquer e mostre se ele é bissexto. """
anoBissexto = int(input("Digite o ano que deseja verificar: "))
anoPorCem = anoBissexto % 100
anoPorQuatrocentos = anoBissexto % 400
if anoPorCem == 0:
    if anoPorQuatrocentos == 0:
        print(f"O ano de {anoBissexto} é bissexto")
    else:
        print(f"O ano de {anoBissexto} não é bissexto")
else:
    print(f"O ano de {anoBissexto} não é bissexto")
    