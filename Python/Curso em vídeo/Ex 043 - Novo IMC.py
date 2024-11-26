""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa e calcule seu IMC e mostre sua classificação segundo a tabela abaixa:

- Abaixo de 18:5: Abaixo do poso
- Entre 18.5 a 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida  """

pesoDoSujeito = float(input("Qual é seu peso atual? "))
alturaDoSujeito = float(input("Qual a sua altura? "))
imc = pesoDoSujeito / (alturaDoSujeito * alturaDoSujeito)
if imc < 18.5:
    print(f"Seu IMC atual é de {imc:.1f}, isso significa que você está abaixo do peso ideal. Procure um médico para avaliar melhor a sua situação")
elif 18.5 < imc <= 25:
    print(f"Seu IMC atual é de {imc:.1f}, isso significa que você está dentro do peso ideal para os parâmetros que forma apresentados.")
elif 25 < imc <= 30:
    print(f"Seu IMC atual é de {imc:.1f}, isso significa que você está com sobrepeso. Procure um médico para avaliar melhor a sua situação")
elif 30 < imc <= 40:
    print(f"Seu IMC atual é de {imc:.1f}, baseado nos parâmetros apresentado, isso pode ser diagnosticado como obesidade. Procure um médico para avaliar melhor a sua situação")
elif imc > 40:
    print(f"Seu IMC atual é de {imc:.1f}, baseado nos parâmetros apresentado, isso pode ser diagnosticado como obesidade mórbida. Procure um médico para avaliar melhor a sua situação")

