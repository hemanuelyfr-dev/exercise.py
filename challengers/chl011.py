#faça um programa que leia a
#largura e a altura de uma 
#parede em metros, calcule a 
#sua area e a quantidade de
#tinta necessaria para 
#pintá-la, sabendo que cada 
#litro de tinta, pinta uma 
#area de 2m².

larg = float(input('Quantos metros de largura tem a parede? '))
alt = float(input('E quantos metros de altura? '))
area = larg * alt
tinta = area / 2
print('A quantidade necessária para pintar a parede é {:.2f} litros'.format(tinta))
