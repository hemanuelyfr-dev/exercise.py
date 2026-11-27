#escreva um programa que 
#converta uma temperatura 
#digitada em °C e converta 
#para °F.

celsius = float(input('Informe a temperatura em graus celsius (°C): '))
fahr = ((9 * celsius) / 5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F'.format(celsius, fahr))