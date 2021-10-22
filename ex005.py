# Programa que exibe o sucesso e o antecessor do numero digitado
numero = int(input('Digite um número: '))
print('O sucessor é \033[1;33m{}\033[m e o antecessor é \033[1;33m{}\033[m'.format(numero + 1, numero - 1))
