""" Ex 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome. """

localizarSilva = str(input("Digite seu nome complete: "))
silvaMaiusculo = localizarSilva.title()
if "Silva" in silvaMaiusculo:
    print(f"Muito prazer {silvaMaiusculo} do clâ Silva")
else:
    print(f"Muito prazer, {silvaMaiusculo}.")
