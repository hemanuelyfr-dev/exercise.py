#escreva um programa que leia
#um valor em metros e o exiba
#convertido em centimetros e
#milimetros.

metros = float(input('Digite o valor em metros:'))
cent = metros * 100
mili = metros * 1000

print('A medida {} correspode a:\n{:.0f}cm\n{:.0f}mm'.format(metros, cent, mili))
