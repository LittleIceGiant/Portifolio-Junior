//Crie um programa que receba três números, calcule e mostre a multiplicação desses números.
algorithm multiplicaNumerosDoUsuario;
var
    double: num1, num2, num3, resultado1;
start
    input("Digite aqui o primeiro número: ")
    read(num1)
    input("Digite aqui o segundo número: ")
    read(num2)
    input("Digite aqui o terceiro número: ")
    read(num3)
    resultado1 <- num1 * num2 * num3
    print("" + num1 + " X " + num2 + " X " + num3 + " = " + resultado1 + "")
end
end_algorithm
