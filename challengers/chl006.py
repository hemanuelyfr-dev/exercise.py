#cria um algoritmo que leia
#um numero e mostre o seu 
#dobro, triplo e raiz 
#quadrada.

numb = int(input('Digite um valor:'))
dobro = numb * 2 
triplo = numb * 3 
rqua = numb ** (1/2)
print('Número: {}\nDobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f}'.format(numb, dobro, triplo, rqua))
