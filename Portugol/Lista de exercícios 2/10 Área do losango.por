//Crie um programa que seja capaz de calcular e mostrar a área de um losango.
//Sabe-se que: A = lado * lado
//A = Área

algorithm areaDoLosango;
var
    float: num1, num2, area;
start
    input("Escreva aqui o lada A: ")
    read(num1)
    input("Escreva aqui o lado B: ")
    read(num2)
    area <- num1 * num2
    print("A área do losango é: ", area)
end
end_algorithm
