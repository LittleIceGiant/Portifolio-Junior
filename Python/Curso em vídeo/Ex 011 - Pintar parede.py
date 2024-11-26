larguraDaParede = float(input("Qual a largura da parede? "))
alturaDaParede = float(input("Qual a altura da parede? "))
areaTotal = alturaDaParede * larguraDaParede
print(f"Você tem a área total de {areaTotal}m², cada metro precisa de 2l de tinta para ser pintado, portanto a quantidade necessária é de {areaTotal / 2:.2f}l de tinta")
