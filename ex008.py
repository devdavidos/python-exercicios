'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
meters = int(input('Digite o valor em metros: '))

print('O valor em metros é: {}m\nEm centímetros: {}cm\nEm milímetros: {}mm.' .format(meters, meters * 100, meters * 1000))