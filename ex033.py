# Programa que mostra qual numero eh maior e qual eh menor entre 3
numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
numero3 = float(input('Digite o terceiro número: '))
if numero1 > numero2:
    if numero1 > numero3:
        print('O número {} é o maior entre os três'.format(numero1))
if numero2 > numero1:
    if numero2 > numero3:
        print('O número {} é o maior entre os três'.format(numero2))
if numero3 > numero1:
    if numero3 > numero2:
        print('O número {} é o maior entre os três'.format(numero3))
if numero1 < numero2:
    if numero1 < numero3:
        print('O número {} é o menor entre os três'.format(numero1))
if numero2 < numero1:
    if numero2 < numero3:
        print('O número {} é o menor entre os três'.format(numero2))
if numero3 < numero1:
    if numero3 < numero2:
        print('O número {} é o menor entre os três'.format(numero3
                                                           ))