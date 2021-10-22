# Programa que calcula o aumento do salario
salario = float(input('Digite o salário: '))
if salario > 1250:
    print('O novo salário, com aumento de 10% é R${}'.format(salario + (10 / 100) * salario))
else:
    print('O nome salário, com aumento de 15% é R${}'.format(salario + (15 / 100) * salario))
