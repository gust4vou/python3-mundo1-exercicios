# Programa que sorteia um aluno para apagar o quadro
import random
primeiro = input('Nome do primeiro aluno: ')
segundo = input('Nome do segundo aluno: ')
terceiro = input('Nome do terceiro aluno: ')
quarto = input('Nome do quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
print('O aluno escolhido foi {}'.format(random.choice(lista)))
