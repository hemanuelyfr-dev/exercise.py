#faça um algoritmo que leia 
#o salario de um funcionario 
#e mostre seu novo salario, 
#com 15% de aumento.

sal = float(input('Digite o seu salário: '))
aum = (sal * 15) / 100

print('Seu novo salário com 15% de aumento: {:.2f}'.format(sal+aum))
