//Crie um programa no qual o usuário possa digitar um número e seja mostrada na tela a tabuada do número digitado.

algorithm tabuada;
var
    int: num1, resultado;
start
    input("Digite o número aqui: ")
    read(num1)
    
    resultado <- num1 * 0
    print("" + num1 + " X 0 = " + resultado + "")

    resultado <- num1 * 1
    print("" + num1 + " X 1 = " + resultado + "")

    resultado <- num1 * 2
    print("" + num1 + " X 2 =" + resultado + "")

    resultado <- num1 * 3
    print("" + num1 + " X 3 = " + resultado + "")

    resultado <- num1 * 4
    print("" + num1 + " X 4 = " + resultado + "")

    resultado <- num1 * 5
    print("" + num1 + " X 5 = " + resultado + "")

    resultado <- num1 * 6
    print("" + num1 + " X 6 = " + resultado + "")

    resultado <- num1 * 7
    print("" + num1 + " X 7 = " + resultado + "")

    resultado <- num1 * 8
    print("" + num1 + " X 8 = " + resultado + "")

    resultado <- num1 * 9
    print("" + num1 + " X 9 = " + resultado + "")

    resultado <- num1 * 10
    print("" + num1 + " X 10 = " + resultado + "")
end
end_algorithm
