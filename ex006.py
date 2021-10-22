# Programa que exibe o dobro, o triplo e a raiz quadrada no numero digitado
numero = int(input('Digite um número: '))
print('O dobro é \033[1;33m{}\033[m, o triplo é \033[1;33m{}\033[m, e a raíz quadrada é \033[1;33m{:.2f}\033[m'.format(numero * 2, numero * 3, numero ** (1/2)))
