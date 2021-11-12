'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
from math import sqrt
number = int(input('Digite um número: '))

print('O número: {}, dobro: {}, triplo: {}, raiz quadrada: {:.1f}' .format(number, number + number, number * 3, sqrt(number)))