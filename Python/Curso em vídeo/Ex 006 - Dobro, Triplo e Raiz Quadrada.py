num1 = int(input("Digite um número: "))
dobro = num1 * 2
triplo = num1 * 3
raiz = num1 ** (1/2)
print(f"Seus resultados são: {num1}, {dobro}, {triplo} e {raiz:.2f}")
print(f"Seus resultados são: {num1}, {num1*2}, {num1*3} e {num1**(1/2):.2f}")
print(f"Seus resultados são: {num1}, {num1*2}, {num1*3} e {pow(num1, (1/2)):.2f}")


'''O Guanbara usou o format de uma forma diferente, ele usou o (.format) para fazer as coisa na aula 7. Bastante interessante.
Fiz três exemplos de como fazer exatamente a mesma coisa para que eu pudesse ter uma referência mais tarde. O terceiro exemplo utilizou a função "power" que serve para calcular a raíz quadrada tão bem quanto nos outros exemplos. Essa função se escreve resumidamente como "pow". Para fazar  o calculo, primeiro se coloca o número do qual será calculada a raiz e depois o número pelo qual o anterior será elevado. '''
