# Programa que exibe o tipo do que foi digitado e os valores verdadeiro ou falso
valor = input('Digite algo: ')

print('O tipo primitivo é {}'.format(type(valor))) # exibe o tipo do que foi digitado
print('Só tem espaços? {}'.format(valor.isspace())) # o que foi digitado é um espaço?
print('É alfa numérico? {}'.format(valor.isalnum())) # o que foi digitado é alfa numérico?
print('É numérico? {}'.format(valor.isnumeric())) # o que foi digitado é numérico?
print('Está em ASCII? {}'.format(valor.isascii())) # o que foi digitado é ASCII?
print('É decimal? {}'.format(valor.isdecimal())) # o que foi digitado é decimal?
print('É um dígito? {}'.format(valor.isdigit())) # o que foi digitado é um digito?
print('É um identificador? {}'.format(valor.isidentifier())) # o que foi digitado é um identificador?
print('É minúsculo? {}'.format(valor.islower())) # o que foi digitado é minúsculo?
print('É maiúsculo? {}'.format(valor.isupper())) # o que foi digitado é maiúsculo?
print('É printável? {}'.format(valor.isprintable())) # o que foi digitado é printável?
print('É alfabético? {}'.format(valor.isalpha())) # o que foi digitado é afabético?
print('É título? {}'.format(valor.istitle())) # o que foi digitado é título?
