nome = input("Digite o seu nome: ")
sobrenome = input("Digite seu sobre nome: ")

nomeCompleto = nome + " " + sobrenome
print(nomeCompleto)

comida = input("O que você gostaria de comer: ")
bebida = input("Qual bebida pra acompanhar: ")
pedido = "Beleza vamos preparar seu  " + comida + "  e vamos pegar sua  " + bebida
#pedido = "Beleza vamos preparar seu  " + comida + "  e vamos pegar sua  " + bebida
print(f"Beleza vamos preparar seu   {comida}    e vamos pegar sua    {bebida}")






# Primeira forma de concatenar texto.
# pedidoCliente = "Beleza. Vamos preparar para comer " + comida + ". E para beber, no capricho vai " + bebida + ". Aguarde seu pedido!"

# Segunda forma de concatenar texto.
# print(f"Vamos preparar para comer {comida}. E para beber no capricho {bebida}. Aguarde seu pedido!")

# Terceira forma de concatenar texto.
#print("Vamos preparar para comer {}. E para beber no capricho {}. Aguarde seu pedido".format(comida, bebida))
