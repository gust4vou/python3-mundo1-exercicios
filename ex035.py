# Programa que diz se 3 retas podem ou nao formar um triangulo
reta1 = int(input('Digite o comprimento da primeira reta: '))
reta2 = int(input('Digite o comprimento da segunda reta: '))
reta3 = int(input('Digite o comprimento da terceira reta: '))
if reta1 + reta2 > reta3:
    if reta1 + reta3 > reta2:
        if reta2 + reta3 > reta1:
            print('As retas podem formar um triângulo!')
        else:
            print('As retas não podem formar um triângulo!')
