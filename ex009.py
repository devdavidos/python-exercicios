'''
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
'''
number = int(input('Insira um número: '))
contador = 1
while (contador <= 10):
    mult = number * contador
    print('{} x {} = {}' .format(number, contador, mult))
    contador = contador + 1