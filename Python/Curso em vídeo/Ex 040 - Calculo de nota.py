""" Crie um programa que leia duas notas d e um aluo e calcule sua nota média, mostrando uma mensagem no final, conforme a média atingida:

- Média abaixo de 5,0: REPROVADO
- Média entre 5,0 e 6,9: RECUPERAÇÃO
- Media 07 ou superior: APROVADO """
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Agora a segunda nota, por favor: "))
notaFinal = (primeiraNota + segundaNota) / 2
if notaFinal < 5:
    print(f"Você foi reprovado. Sua media foi de {notaFinal} pontos")
if 5 <= notaFinal < 7:
    print(f"Você entrou em recuperação: Sua média foi de {notaFinal} pontos")
'''if 5 >= notaFinal < 7:
    print(f"tentativa 2: Sua média foi de {notaFinal} pontos")'''
if notaFinal >= 7:
    print(f"Você foi aprovado. Sua média foi de: {notaFinal} pontos")
