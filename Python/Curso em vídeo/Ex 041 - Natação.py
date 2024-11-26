""" Ex 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostra sua categoria,
conforme a idade.

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: MASTER """
from datetime import datetime, timedelta, date
hoje = date.today( ).year
atleta = int(input("Qual o seu ano de nascimento? "))
categoria = hoje - atleta
if categoria <= 9:
    print(f"O(a) atleta {categoria} anos e se encontra na categoria MIRIM")
elif categoria <= 14:
    print(f"O(a) atleta {categoria} anos e se encontra na categoria INFANTIL")
elif categoria <= 19:
    print(f"O(a) atleta {categoria} anos e se encontra na categoria JUNIOR")
elif categoria <= 20:
    print(f"O(a) atleta {categoria} anos e se encontra na categoria SÊNIOR")
elif categoria > 20:
    print(f"O(a) atleta {categoria} anos e se encontra na categoria MASTER")
