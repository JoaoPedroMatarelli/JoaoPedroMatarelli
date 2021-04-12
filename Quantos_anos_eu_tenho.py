import datetime

nascimento = int(input("digite seu ano de nascimento: "))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento
print(f"Nesse ano você completa {idade}")

