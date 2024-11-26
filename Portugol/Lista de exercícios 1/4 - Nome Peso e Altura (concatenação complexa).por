// Crie um programa em que o usuário possa digitar, seu nome, seu peso, sua altura e sua idade e isso tudo seja exibido em uma mensagem final seguindo este exemplo:

//O seu nome é: <nome>
//Seu peso: <peso>
//Sua altura: <altura>
//Sua idade: <idade>

algorithm nomePesoAltura;
var
    string: nome;
    float: peso, altura, idade;
start
    input("Qual o seu nome?: ")
    read(nome)
    input("Quanto você pesa? Prometo que ficará só entre nós: ")
    read(peso)
    input("Qual a sua altura?: ")
    read(altura)
    input("Qual a sua idade?: ")
    read(idade)
    print("Se nome é: " + nome + ". \nSeu peso é: " + peso + " kg.\nSua altura é: " + altura + ". \nSua idade é: " + idade + ".")
end
end_algorithm
