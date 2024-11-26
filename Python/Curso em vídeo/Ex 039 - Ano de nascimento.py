"""Ex 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar no serviço milita.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu program também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
hoje = date.today().year
candidato = int(input("Digite seu ano de seu nascimento: "))
idade = hoje - candidato
print(f"Quem nasceu em {candidato} tem {idade} anos")
if idade < 18:
    faltante = 18 - idade
    print(f"Faltam {18 - idade} anos para a idade de se alistar. Você deverá se alistar em {hoje + faltante}")
elif idade == 18:
    print("Você está na idade exata (18 anos) para se alistar")
elif idade > 18:
    sobra = idade - 18
    print(f"Você passou {idade - 18} anos da idade de alistamento. Você deveria ter se alistado em {hoje - sobra}")
