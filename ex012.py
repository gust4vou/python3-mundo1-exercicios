# Programa que exibe o preco do produto com desconto
produto = float(input('Digite o preço do produto: '))
print('O novo preço com 5% de desconto é {}'.format(produto - ((5/100) * produto)))
