pontoDePartida = int(input("Digite o número do qual deseja saber a tabuada: "))
i = 0
while i < 11:
    resultadoFinal = pontoDePartida * i
    #   print(f"{pontoDePartida} x {i} = {pontoDePartida * i}") assim também funciona
    print(f"{pontoDePartida} x {i} = {resultadoFinal}")
    i = i + 1
print("Aí está sua tabuada")
