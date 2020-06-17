'''Programa que utiliza um dict que lê dados de entrada do usuário. O usuário
deve entrar com os dados de uma pessoa como nome, idade e cidade onde mora.'''

nome = input('Digite o seu nome: ')

idade = int(input('Digite sua idade: '))

cidade = input('Digite a sua cidade: ')

dados = {'Nome':nome, 'Idade':idade, 'Cidade':cidade}

print(dados)
