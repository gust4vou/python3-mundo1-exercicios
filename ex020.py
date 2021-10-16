# Programa que mostra a ordem de apresentação de um trabalho
import random
primeiro = input('Digite o nome de um aluno: ')
segundo = input('Digite o nome de um aluno: ')
terceiro = input('Digite o nome de um aluno: ')
quarto = input('Digite o nome de um aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
random.shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))
