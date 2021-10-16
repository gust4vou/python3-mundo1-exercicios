# Programa que le um numero real e devolve a parte inteira dele
from math import trunc
numero = float(input('Digite um número real: '))
print('A parte inteira de {} é {}'.format(numero, trunc(numero)))
