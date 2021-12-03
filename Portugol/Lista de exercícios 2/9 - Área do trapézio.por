//Crie um programa que seja capaz de calcular e mostrar a área de um trapézio
//Sabe-se que: A = ((base maior + base menor) * altura) /2
//A = Área

algorithm areaDoTrapezio;
var
    float: baseMenor, baseMaior, alturaDoTrapezio, somaDasBase, baseVezesAltura, resultado;
start
    input("Qual a base menor?: ")
    read(baseMenor)
    input("Qual a base maior?: ")
    read(baseMaior)
    input("Qual a altura?: ")
    read(alturaDoTrapezio)
    somaDasBases <- baseMenor + baseMaior
    baseVezesAltura <- somaDasBases * altura
    resultado <- baseVezesAltura / 2
    print("A área do trapézio é: ", resultado)
end
end_algorithm
