num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
soma = num1 + num2
subs = num1 - num2
mult = num1 * num2
div = num1 / num2
div_int = num1 // num2
exp = num1 ** num2

print('a soma: {}\no produto: {}\na divisão: {}'.format(soma, mult, div))
print('a divisão inteira {}\ne a potencia {} \n'.format(div_int, exp))