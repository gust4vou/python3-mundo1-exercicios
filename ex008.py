# Programa que converte de metros para centimetros e depois milimetros
valor = float(input('Digite uma media em metros: '))
print('O valor em centímetros é \033[1;34m{}\033[m, em milímetros é \033[1;34m{}\033[m'.format(valor * 100, valor * 1000))
