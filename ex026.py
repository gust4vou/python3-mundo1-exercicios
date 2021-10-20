# Programa que le uma frase e diz:
# quantas vezes aparece a letra "a",
# em que posicao ela aparece a primeira vez,
# em que posicao ela aparece a ultima vez

frase = str(input('Digite uma frase: '))
frase = frase.lower()
print('A letra "a" aparece {} vezes na frase!'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posicao {}!'.format(frase.find('a')))
print('A letra "a" aparece pela ultima vez na posicao {}!'.format(frase.rfind('a')))
