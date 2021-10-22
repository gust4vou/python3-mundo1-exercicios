# Programa que exibe o tipo do que foi digitado e os valores verdadeiro ou falso
valor = input('Digite algo: ')

print('O tipo primitivo é \033[4;34m{}\033[m'.format(type(valor))) # exibe o tipo do que foi digitado
print('Só tem espaços? \033[4;34m{}\033[m'.format(valor.isspace())) # o que foi digitado é um espaço?
print('É alfa numérico? \033[4;34m{}\033[m'.format(valor.isalnum())) # o que foi digitado é alfa numérico?
print('É numérico? \033[4;34m{}\033[m'.format(valor.isnumeric())) # o que foi digitado é numérico?
print('Está em ASCII? \033[4;34m{}\033[m'.format(valor.isascii())) # o que foi digitado é ASCII?
print('É decimal? \033[4;34m{}\033[m'.format(valor.isdecimal())) # o que foi digitado é decimal?
print('É um dígito? \033[4;34m{}\033[m'.format(valor.isdigit())) # o que foi digitado é um digito?
print('É um identificador? \033[4;34m{}\033[m'.format(valor.isidentifier())) # o que foi digitado é um identificador?
print('É minúsculo? \033[4;34m{}\033[m'.format(valor.islower())) # o que foi digitado é minúsculo?
print('É maiúsculo? \033[4;34m{}\033[m'.format(valor.isupper())) # o que foi digitado é maiúsculo?
print('É printável? \033[4;34m{}\033[m'.format(valor.isprintable())) # o que foi digitado é printável?
print('É alfabético? \033[4;34m{}\033[m'.format(valor.isalpha())) # o que foi digitado é afabético?
print('É título? \033[4;34m{}\033[m'.format(valor.istitle())) # o que foi digitado é título?
