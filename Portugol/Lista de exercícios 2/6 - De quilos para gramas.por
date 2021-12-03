//Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.
algorithm quilosParaGramas;
var
    float: quilos1, gramas1;
start
    input("Escreva aqui o seu peso em quilogramas: ")
    read(quilos1)
    gramas1 <- quilos1 * 1000
    print(gramas1)
end
end_algorithm
