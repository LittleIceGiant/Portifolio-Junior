""" Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o Flag)  """

count = sum1 = 0
while True:
    value = int(input("Enter the desired value: "))
    if value == 999:
        break
    sum1 += value
    count += 1
print(f"The sum between the {count} numbers entered is {sum1} ")
