#faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possiveis sobre ele.
char = input('Type something:')
print('The primitive type of this value is  ',type(char))
print('Are there only spaces? ',char.isspace())
print('Is it a number? ', char.isnumeric())
print('Is it an alphabetic one? ', char.isalpha())
print('Is it an alphanumeric?', char.isalnum())
print('Is it in uppercase?', char.isupper())
print('Is it in lowercase?', char.islower())
print('Is it capitalized?', char.istitle())

