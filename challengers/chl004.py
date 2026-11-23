#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Type something: ')
print('The type primitivo is ', type(n))
print('Is it a number', n.isnumeric())
print('Is it a letter', n.isalpha())
print('Is it alphanumeric', n.isalnum())
print('Is it uppercase', n.isupper())
print('Is it lowercase', n.islower())
print('Is it a title', n.istitle())
print('Is it a space', n.isspace())
print('Is it a digit', n.isdigit())
print('Is it a decimal', n.isdecimal())
print('Is it an identifier', n.isidentifier())
print('Is it printable', n.isprintable())
print('Is it ascii', n.isascii())


