import time
nome = input("Digite seu nome: ")
disciplina = input("Digite o nome da disciplina: ")
nota1 = float(input("Digite a nota da prova: "))
nota2 = float(input("Digite a nota do trabalho pratico: "))
nota3 = float(input("Digite a nota do projeto final: "))
time.sleep(0.4)
media = (nota1 + nota2 + nota3) / 3
print('vamos calcular')
time.sleep(2)
print(f"A sua media é:{media:.2f}")
time.sleep(1.5)
if media>= 7:
  print("Voce foi aprovado!")
else:
  print("voce foi reprovado!")
  pontos_Que_Faltaram = float(7 - media)
  print(f'faltaram {pontos_Que_Faltaram} pontos para voce ser aprovado')