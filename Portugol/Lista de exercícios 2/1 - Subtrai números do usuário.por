//Crie um programa que receba dois números digitados pelo usuário, calcule e mostre a subtração do primeiro número pelo segundo.
algorithm subtraiNumerosDoUsuario;
var
    double: primeiroNumero1, segundoNumero2, subtracao1;
start
    input("Escreva aqui o primeiro número: ")
    read(primeiroNumero1)
    input("Escreva aqui o segundo número: ")
    read(segundoNumero2)
    subtracao1 <- primeiroNumero1 - segundoNumero2
    print("" + primeiroNumero1 + " - " + segundoNumero2 + " = " + subtracao1 + ".")
end
end_algorithm
