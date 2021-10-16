# Programa que calcula seno, cosseno e tangente de um angulo
from math import sin, cos, tan
angulo = int(input('Digite um angulo: '))
print('O seno do angulo {} é {}'.format(angulo, sin(angulo)))
print('O cosseno do angulo {} é {}'.format(angulo, cos(angulo)))
print('A tangente do angulo {} é {}'.format(angulo, tan(angulo)))
