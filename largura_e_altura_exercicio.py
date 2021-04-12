largura = float(input('Digite a Largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area_Total = altura * largura
print(f'A area total da parede é{area_Total}m ')
print('sabendo que com 1 litro de tinta pinta-se 2 metros quadrado')
litros = float(area_Total / 2)
print(f'Serão nessesarios {litros} litros de pinta para pintar a parede de area {area_Total}m')
