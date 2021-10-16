# Programa que calcula o preço a se pagar pelo aluguel de um carro
kilometragem = float(input('Quantos quilometros foram percoridos? '))
dias = int(input('O carro foi alugado por quantos dias? '))
print('O preço a se pagar pelo aluguel é R${}'.format((60 * dias) + (0.15 * kilometragem)))
