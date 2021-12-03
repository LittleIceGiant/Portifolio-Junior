//Crie um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, no contexto em que estamos, considere usar peso 2 para a primeira nota e peso 3 para a segunda nota.

//Media: (nota1 * peso 2) + (nota2 * peso 3)
//Dividido por: peso + peso 3

algorithm mediaPonderada;
var
    float: nota1, nota2, media1, media2, media3, peso, resultado1;
start
    input("Dê entrada na primeira nota: ")
    read(nota1)
    input("Dê entrada na segunda nota: ")
    read(nota2)
    media1 <- nota1 * 2
    media2 <- nota2 * 3
    media3 <- media1 + media2
    peso <- 2 + 3
    resultado1 <- media3 / peso
    imprima("A média ponderada é: ", resultado1)
end
end_algorithm
