# Programa que calcula a hipotenuza
from math import hypot
catetoOpo = int(input('Digite o cateto oposto: '))
catetoAdj = int(input('Digite o cateto adjacente: '))
print('A hipotenuza é {:.2f}'.format(hypot(catetoAdj, catetoOpo)))
