# Programa que le o nome de uma cidade e diz se  comeca ou nao com "Santo"

cidade = str(input('Digite o nome de uma cidade: '))
cidade = cidade.lower().split()[0]
print('santo' in cidade)
