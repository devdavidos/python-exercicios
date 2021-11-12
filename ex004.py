'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
'''

word = input('Digite algo: ')

print(type(word))
print(word.isalnum())
print(word.isalpha())
print(word.islower())
print(word.isupper())