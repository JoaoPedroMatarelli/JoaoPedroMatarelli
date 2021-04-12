# o tipo de dados serve para
#valor = 10
#print(type(valor))
#valor2 = 10.5
#print(type(valor2))
#valor3 = 'ana'
#print(type(valor3))
#valor4 = True
#print(type(valor4))
valor = int(input("Digite o primeiro valor"))
valor2 = int(input("Digite o segundo valor"))
soma = valor + valor2
subtraçao = valor - valor2
multiplicaçao = valor * valor2
divisao = valor / valor2

print(f"O resultado da soma:{soma} ")
print(f"O resultado da subtraçao: {subtraçao}")
print(f"o resultado da multiplicaçao: {multiplicaçao}")
print(f"O resultado da divisao: {divisao}")

# ordem de prepotencia


Materia = input('Digite o nome da materia')
nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
nota3 = float(input('Digite a terceira nota'))
nota4 = float(input('Digite a quarta nota'))
Nota =  (nota1 + nota2 + nota3 + nota4) / 4


print(f"Em {Materia} você fico com {Nota:.2} de nota final.")
#variavel com dois ponto