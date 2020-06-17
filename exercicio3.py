'''Faça um programa que leia 4 notas, mostre as notas e a média na tela.'''
notas = []

nota1 = float(input('Digite a primeira nota: '))
notas.append(nota1)

nota2 = float(input('Digite a segunda nota: '))
notas.append(nota2)

nota3 = float(input('Digite a terceira nota: '))
notas.append(nota3)

nota4 = float(input('Digite a quarta nota: '))
notas.append(nota4)

print(notas)

media = float(input('A média é: {}'. format(sum(notas)/len(notas))))
