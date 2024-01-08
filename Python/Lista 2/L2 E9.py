#Crie um programa que seja capaz de calcular e mostrar a área de um
#trapézio.
#Sabe-se que: A = ((base maior + base menor) * altura) /2
#A = Área

print('Qual o valor da base maior?')
maior = float(input())
print('Qual o valor da base menor?')
menor = float(input())
print('Qual a altura?')
altura = float(input())
area1 = (maior + menor) * altura / 2
print('A área toral do trapézio é de: ',area1)