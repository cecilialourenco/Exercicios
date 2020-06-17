'''1 - Programa que utiliza um dict que lê dados de entrada do usuário.
O usuário deve entrar com os dados de uma pessoa como nome, idade e cidade onde
mora. Esses dados deverão ser adicionados em uma lista.'''
'''2 - Perguntar ao usuário se ele deseja adicionar uma nova pessoa. Após
adicionar dados de algumas pessoas, todos os dados de cada pessoa terão que ser
impressos de forma organizada.'''

pergunta = 'sim'
pessoas = []

while (pergunta == 'sim'):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidade = input('Digite a sua cidade: ')
    dados = {'Nome': nome, 'Idade': idade, 'Cidade': cidade}

    pessoas.append(dados)

    pergunta = input('Deseja adicionar uma nova pessoa? ')

for pessoa in pessoas:
    for chave, valor in pessoa.items():
        print(chave + ":", valor)

    print('')
