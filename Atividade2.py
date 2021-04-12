import time
primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero : '))
terceiro = int(input('Terceiro numero: '))
time.sleep(1)
maior = primeiro
if (segundo > maior):
  maior = segundo
if (terceiro > maior):
  maior = terceiro
time.sleep(1)
print(f'Maior:{maior} ')


menor = primeiro
if (segundo < menor):
  menor = segundo
if (terceiro < menor):
  menor = terceiro

time.sleep(1)
print(f'Menor:{menor}')