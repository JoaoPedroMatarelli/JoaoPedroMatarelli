from time import sleep
valor_Casa = int(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salario"))
tempo = int(input("Em quantos anos voce vai pagar: "))
tempo_Em_Messes = tempo * 12
valor_Da_Parcela = valor_Casa / tempo_Em_Messes
salario_30 = salario * 0.30
sleep(2)
if salario_30>= valor_Da_Parcela:
  print("O emprestimo foi aprovado!")
  print(f"O valor da parcela vai ser: R${valor_Da_Parcela}")
else:
  print("O emprestimo foi negado!")
  print("O valor da parcela ultrapassou 30% do seu salario")
  print(f"""
Os 30% do seu salario equivale a R${salario_30}
E o valor da parcela equivale a R${valor_Da_Parcela}
Então o valor da parcela ultrapassou R${valor_Da_Parcela - salario_30}.
Por isso o emprestimo foi negado""")