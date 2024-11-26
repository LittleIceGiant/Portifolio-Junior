#Crie um programa que permita que o usuário digite 10 itens que
#sonha ter e estes itens sejam mostrados no final.

sonhosQueJaSonhei = []
i = 0 
while(i <= 9):
    tela = print('Quais são os 10 produtos de nossa loja que você mais deseja? Comece pelo começo')
    item = input(str())
    sonhosQueJaSonhei.append(item)
    i = i + 1
    print(sonhosQueJaSonhei)