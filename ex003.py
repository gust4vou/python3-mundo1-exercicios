# Programa que faz a soma de dois numeros
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2

print('A soma de \033[1;31m{}\033[m e \033[1;31m{}\033[m é igual a \033[1;32m{}\033[m'.format(n1, n2, soma))
