# Programa que le um numero de 0 a 9999 e exibe cada um dos digitos separados

numero = str(input('Digite um numero de 0 a 9999: '))
print('unidade: {}'.format(numero[3:4]))
print('dezena: {}'.format(numero[2:3]))
print('centena: {}'.format(numero[1:2]))
print('milhar: {}'.format(numero[:1]))
