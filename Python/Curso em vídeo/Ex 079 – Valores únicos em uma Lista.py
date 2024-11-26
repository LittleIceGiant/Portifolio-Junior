""" Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. """
letsContinue = "S"
controlVal = 0
newList = []
while letsContinue == "S":
    controlVal = int(input("Digite o número desejado: "))
    if controlVal in newList:
        print("O valor não pode ser adicionado pois já existe na lista")
    else:
        newList.append(controlVal)
    letsContinue = str(input("Deseja continuar? [S/N]: ")).upper().strip( )
newList.sort()
print(f"Os valores digitados foram: {newList}")