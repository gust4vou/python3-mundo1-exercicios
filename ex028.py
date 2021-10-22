# Programa que sorteia 1 numero de 0 a 5 e diz se o usuario acertou ou nao o palpite
from random import randint
palpite = int(input('Dê o seu palpite de 0 a 5: '))
numeroRandom = randint(0, 5)
print('O número sorteado foi {}'.format(numeroRandom))
if palpite == numeroRandom:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Tente novamente')
