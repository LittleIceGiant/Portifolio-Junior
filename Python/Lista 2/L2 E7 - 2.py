#Crie um programa que permita que o usuário digite os valores de 5
#itens em seu carrinho virtual de compras da empresa “Lojão do Pai”,
#calcule e mostre o total.

preco = []
total = 0
i = 1
while (i <= 5):
  tela = print("Digite o item de número", i)
  produto = float(input())
  preco.append(produto)
  print(preco)
  i = i + 1
  print('Total: ', sum(preco))

#total = preco[0] + preco[1] + preco[2] + preco[3] + preco[4]
# print('Total: ', total) 
# A função 'sum' server para somar os valores de dentro de uma coleção (listas, tuplas ou dicionários). Assim eu poso simplificar o ato de imprimir o valor total ali em cima. muito bom.