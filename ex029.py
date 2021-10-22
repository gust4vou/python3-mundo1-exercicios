# Programa que le a velocidade de um carro e mostra se ele tomou multa ou nao
velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado!')
    print('O valor da multa foi de R${}'.format((velocidade - 80) * 7))
else:
    print('Você está dentro do limite de velocidade!')

