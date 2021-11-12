'''
Desenvolva um programa que leia as duas notas de um aluno.
Calcule e mostre a sua média.
'''
testGradeOne = float(input('Digite a nota da primeira prova: '))
testGradeTwo = float(input('Digite a nora da segunda prova: '))

print('1° nota: {}, 2° nota: {}, média: {:.1f}' .format(testGradeOne, testGradeTwo, (testGradeOne + testGradeTwo) / 2))