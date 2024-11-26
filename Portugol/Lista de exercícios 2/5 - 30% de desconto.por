//Crie um programa que receba o preço de um produto, calcule e mostre o novo preço do produto após receber 30% de desconto.

algorithm 30DeDesconto;
var
    double: valorDoProduto, 30porcento, desconto, resultadoFinal;
start
    input("Qual o valor do produto?: ")
    read(valorDoProduto)
    30porcento <- 30 /100
    desconto <- valorDoProduto * 30porcento
    resultado <- valorDoProduto - desconto
    print("O valor com desconto é de: ", resultado)
end
end_algorithm
