# Programa que le um nome completo e exibe na tela:
# todas as letras maiusculas,
# todas minusculas,
# quantas letras tem (sem considerar os espacos),
# quantas letras tem o primeiro nome

nomeCompleto = str(input('Digite o nome completo: '))
print(nomeCompleto.upper())
print(nomeCompleto.lower())
print(len(nomeCompleto.replace(" ", "")))
print(nomeCompleto.split()[0])


#frase = '      gustavo da Silva Moura     '
#print(frase[8:])
#print(len(frase))
#print(frase.count('o',0,8))
#print(frase.find('a')) # mostra a primeira posicao da ocorrencia do caractere 'a'
#print(frase.rfind('a')) # mostra a ultima posicao da ocorrencia do caractere 'a'
#print('Gustavo' in frase)
#print('Caroline' in frase) # procura na frase
#print(frase.replace('Gustavo', 'GUSTAVO')) # troca uma pela outra
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize()) # coloca a primeira letra em maiusculo
#print(frase.title()) # faz o capitalize pra cada palavra na string
#print(frase.strip()) # remove os espacos inuteis no comeco e no fim da string
#print(frase.rstrip()) # remove somente os espacos da direita
#print(frase.lstrip()) # remove somente os espacos da esquerda
#print(frase.split()[0])
#print(' '.join(frase))