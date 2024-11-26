""" Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e as condições de pagamento:

- À vista no dinheiro ou cheque: 10% de desconto.
- Á vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros. """

valorInicial = float(input("Valor do produto: "))
formaPagamento = int(input("Escolha a forma de pagamento: \n1 - Dinheiro \n2 - À vista no cartão\n3 - Até 2x no cartão \n4 - 3x ou mais no cartão\nDigite o número da opção: "))
if formaPagamento == 1:
  valorFinal = valorInicial * (10/100)
  print(f"Valor da compra (R${valorInicial:.2f}) menos desconto de 10% (R${valorFinal:.2f}).\nTotal a pagar: R${valorInicial - valorFinal:.2f}")
if formaPagamento == 2:
  valorFinal = valorInicial * (5/100)
  print(f"Valor da compra (R${valorInicial:.2f}) menos desconto de 5% (R${valorFinal:.2f}).\nTotal a pagar: R${valorInicial - valorFinal:.2f}")
if formaPagamento == 3:
  print(f"Total a pagar: R${valorInicial}\nA forma de pagamento escolhida não proporciona desconto.")
if formaPagamento == 4:
  valorFinal = valorInicial * (20/100)
  print(f"Valor do produto (R${valorInicial:.2f}) mais 20% de juros (R${valorFinal:.2f}).\nTotal á pagar: R${valorInicial + valorFinal:.2f}")
