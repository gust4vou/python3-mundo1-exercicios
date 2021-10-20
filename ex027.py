# Programa que le um nome completo e mostra o primeiro e o ultimo nome separadamente

nome = str(input('Digite o nome completo: '))
print('primeiro: {}'.format(nome.split()[0]))
print('ultimo: {}'.format(nome.split()[-1]))
