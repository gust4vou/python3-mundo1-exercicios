# Programa que calcula a area da parede e quantos litros de tinta precisaria para pinta-la
largura = float(input('Qual a largura em metros? '))
altura = float(input('Qual a altura em metros? '))
print('A área da parede é {}. Para pintá-la você precisa de {} litros de tinta.'.format(largura * altura, (largura * altura)/2))
