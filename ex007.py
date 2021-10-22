# Programa que calcula a media entra duas notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('A média é \033[1;32m{}\033[m'.format(media))
else:
    print('A média é \033[1;31m{}\033[m'.format(media))
