#Crie um programa no qual o usuário possa digitar um número e seja mostrada na tela a tabuada do número digitado.

print('Vamos fazer umas tabuadas diferênciadas, crianças? Digite o número que nós fazemos o resto')
numero = int(input())
i = 0
conta = ()
while (i <= 10):
    conta = numero * i
    print(' ',  numero, 'X', i, '=', conta, ' ')
    i = i + 1
print('Aí está a sua taboada, jovem gafanhoto')