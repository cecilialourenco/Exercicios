'''Jogo da Adivinhação com três opções de níveis que dão direito a 5, 10 ou 20 tentativas.'''

numero_secreto = 42
pontuacao = 1000

print('Pontuação inicial: 1000 pontos.')

nivel = int(input('Em qual nivel você quer jogar: '))
if(nivel == 1):
    tentativas = 20
elif (nivel == 2):
    tentativas = 10
elif (nivel == 3):
    tentativas = 5

for rodada in range(1, tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, tentativas))

    chute = int(input('Digite o seu número: '))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    pontuacao = abs(pontuacao - (chute - numero_secreto))

    if(acertou):
        print('Você acertou!')
        print('Você terminou com {} pontos!'. format(pontuacao))
        break #se não colocar o break o jogo vai continuar até rodada = total_de_tentativas
    elif(maior):
        print('Você errou! O seu chute foi maior que o número secreto.')
        print('Nova pontuação: {} pontos.'. format(pontuacao))
    elif(menor):
        print('Você errou! O seu chute foi menor que o número secreto.')
        print('Nova pontuação: {} pontos.'. format(pontuacao))

print("Fim do jogo!")
