//Crie um programa em que o usuário possa digitar, o dia, mês e o ano de nascimento de uma pessoa e isso tudo seja exibido em uma mensagem final usando a tecnologia “concatenação complexa”, seguindo este exemplo:
//Data de nascimento: <DD>/<MM>/<AA>
algorithm diaMesAno;
var
   int: dia, mes, ano; 
start
    input("Qual é seu dia de nascimento?: ")
    read(dia)
    input("Em que mês você nasceu?: ")
    read(mes)
    input("Em que ano você nasceu?: ")
    read(ano)
    print("" + dia + "/" + "/" + mes + "/" + ano + "")
end
end_algorithm
