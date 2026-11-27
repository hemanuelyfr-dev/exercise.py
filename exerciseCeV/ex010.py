valor = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = 3.27
dol_conv = valor / dolar
print('Com R${:.2f} você pode comprar US${:.2f}'.format(valor, dol_conv))
