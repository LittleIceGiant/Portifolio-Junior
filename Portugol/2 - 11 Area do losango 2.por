//Crie um programa que seja capaz de calcular e mostrar a área de um losango:
//Sabe-se que: A = (diagonal maior * diagonal menor) /2
//A = Área

algorithm Losango;
var
    double: maior, menor, total, area;
start
    input("Qual a base maior?: ")
    read(maior)
    input("Qual a base menor?: ")
    read(menor)
    total <- maior * menor
    area <- total / 2
end
end_algorithm
