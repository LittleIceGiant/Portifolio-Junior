""" Crie um program que leia vários númeres inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

simOuNao = "S"
entrada = 0
cont = 1
acum = 0
maior = 0
menor = 0
quantidade = 0

entrada = int(input("Digite um número: "))
maior = entrada
menor = entrada
simOuNao = str(input("Deseja continuar? S/N: ")).upper()
acum += entrada
while simOuNao == "S":
    entrada = int(input("Digite um número: "))
    acum += entrada
    cont += 1
    if entrada > maior:
        maior = entrada
    if entrada < menor:
        menor = entrada
    simOuNao = str(input("Deseja continuar? S/N: ")).upper()
print(f"O maior número digitado foi: {maior}"
      f"\nO menor número digitado foi: {menor}"
      f"\nA média foi de: {acum / cont}")
