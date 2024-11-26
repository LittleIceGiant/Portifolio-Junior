""" Refaça o desafio 35 (o desafio dos triângulos) acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: Todos os lados diferentes """

ladoA = float(input("Qual o tamanho do lado A? "))
ladoB = float(input("Qual o tamanho do lado B? "))
ladoC = float(input("Qual o tamanho do lado C? "))
if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    if ladoA == ladoB and ladoA == ladoC:
        print("Os valores digitados podem formar um triângulo Equilátero")
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoA and ladoB != ladoC and ladoC != ladoA and ladoC != ladoB:
        print("Os valores digitados podem formar um triângulo Escaleno")
    else:
        print("Os valores digitados podem formar um triângulo Isósceles")
else:
    print("Os valores digitados NÃO são capazes de formar  uma triângulo")

"""elif ladoA == ladoB and ladoA != ladoC or ladoA == ladoC and ladoA != ladoB or ladoB == ladoA and ladoB != ladoC:"""

