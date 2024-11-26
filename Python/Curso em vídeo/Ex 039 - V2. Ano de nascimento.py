"""Ex 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar no serviço milita.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu program também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date, datetime
diaNascimento = int(input("Informe o dia de seu nascimento: "))
mesNascimento = int(input("Agora informe o mês: "))
anoNascimento = int(input("Por fim, informe o ano: "))
da_ta = f"{diaNascimento}/{mesNascimento}/{anoNascimento}"
"""date2 = datetime.strptime(dataCompleta,'%d/%m/%Y').date()"""
dataFormatada = da_ta.strptime('%d/%m/%Y')
print(dataFormatada)