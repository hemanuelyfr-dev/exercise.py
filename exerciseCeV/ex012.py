preço = float(input('Digite o valor do produto: R$'))
desc = (preço * 5) / 100

print('O novo preço do produto com desconto de 5% é: R${:.2f}'.format(preço - desc))
