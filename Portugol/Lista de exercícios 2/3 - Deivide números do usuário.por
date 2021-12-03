//Crie um programa que receba dois números digitados pelo usuário, calcule e mostre a divisão do primeiro número pelo segundo. Sabese que o segundo número não pode ser zero, portanto é necessário se preocupar com validações.

algorithm divideNumerosDoUsuario;
var
    double: num1, num2, resultado1;
start
    input("Digite o primeiro número: ")
    read(num1)
    input("Digite o segundo número: ")
    read(num2)
    resultado1 <- num1 / num2
    se(num2 <= 0){
        imprima("O segundo número tem que ser maior que zero")
    }
    senao{
        imprima("" + num1 + " ÷ " + num2 + " = " + resultado1 + "")
    }
end
end_algorithm
