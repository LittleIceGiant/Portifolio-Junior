#Crie um programa no qual o usuário possa digitar o salário mínimo e o valor do salário do funcionário, calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.

print('Qual o valor atual do salário mínimo?')
minimo = float(input())
print('Qual o salário do funcionário?')
real = float(input())
diferenca = real / minimo
print('O valor real do salário do funcionário equivale a', diferenca, 'salários mínimos')