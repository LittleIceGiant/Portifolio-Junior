//Crie um programa no qual o usuário possa digitar o salário mínimo e o valor do salário do funcionário, calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.

algorithm calculoDeSalario;
var
    double: salarioMinimo, salarioReal, resultado;
start
    input("Qual o valor do salário mínimo?: ")
    read(salarioMinimo)
    input("Qual o salário real do funcionário?: ")
    read(salarioReal)
    resultado <- salarioReal / salarioMinimo
    print("O salário do funcionário equivale á ", resultado)
end
end_algorithm
