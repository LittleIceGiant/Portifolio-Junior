metragem = float(input("Digite o valor em metros: "))
centimetros = float(metragem * 100.0)
milimetros = float(metragem * 1000.0)
print(f"As converções para CM e MM deram os seguintes resultados:\n{centimetros} Centimetros\n{milimetros} Milimetros")
print(
    f"As converções para CM e MM deram os seguintes resultados:\n{metragem * 100:.3f} Centimetros\n{metragem * 1000:.3f} Milimetros")
