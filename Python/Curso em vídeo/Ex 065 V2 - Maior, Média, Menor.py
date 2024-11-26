""" Crie um program que leia vários númeres inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. """

simOuNao = "S"
cont = 0
acum = 0
quantidade = int(input("Você vai dar entrada em quantos valores? "))
entrada = int(input("1º valor: "))
maior = entrada
menor = entrada
cont += 1
acum += entrada
while simOuNao == "S":
    while cont != quantidade:
        cont += 1
        entrada = int(input(f"{cont}º valor: "))
        acum += entrada
        if entrada > maior:
            maior = entrada
        if entrada < menor:
            menor < entrada
    if cont == quantidade:
        simOuNao = str(input("Deseja adicionar mais valores? S/N" )).upper()
        if simOuNao == "S":
            novoValor = int(input("Quantos valores deseja adicionar? "))
            quantidade += novoValor
print(f"O maior valor digitado foi: {maior}"
      f"\nO menor valor digitado foi: {menor}"
      f"\nE a média dos valores digitados foi: {acum / cont:.0f}")