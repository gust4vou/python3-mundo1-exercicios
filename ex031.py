# Programa que calcula o preco da passagem
distancia = int(input('Digite a distância em km: '))
if distancia <= 200:
    print('O valor da passagem é de {}'.format(distancia * 0.50))
else:
    print('O valor da passagem é de {}'.format(distancia * 0.45))
