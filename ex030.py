# Programa que le um numero inteiro e mostra se eh par ou impar
numero = int(input('Digite um número inteiro: '))
if numero % 2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar'.format(numero))
