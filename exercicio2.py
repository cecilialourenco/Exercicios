'''Faça um programa que leia dados do usuário (nome, sobrenome, idade) adicione
em uma lista e imprima seus elementos na tela.'''

dados = []

nome = input('Digite o seu nome: ')
dados.append(nome)
sobrenome = input('Digite o seu sobrenome: ')
dados.append(sobrenome)
idade = int(input('Digite a sua idade: '))
dados.append(idade)

print(dados)
