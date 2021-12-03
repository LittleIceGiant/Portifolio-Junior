//Crie um programa que permita que o usuário digite os valores de 5 itens em seu carrinho virtual de compras da empresa “Lojão do Pai”, calcule e mostre o total.
algorithm somaDeProdutos;
var
    double: item1, item2, item3, item4, item5, resultado1;
start
    input("Produto 1: ")
    read(item1)
    input("Produto 2: ")
    read(item2)
    input("Produto 3: ")
    read(item3)
    input("Produto 4: ")
    read(item4)
    input("Produto 5: ")
    read(item5)
    resultado1 <- item1 + item2 + item3 + item4 + item5
    print("O valor total é de: ", resultado1)
end
end_algorithm
