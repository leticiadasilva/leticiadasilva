import random
from funcoesjogo import boas_vindas

boas_vindas()

print(f'Seu desafio será acertar um número escolhido aleatoriamente por mim.'
        '\nVocê deve digitar um número entre 1 e 100.')

numero_secreto = (random.randint(1, 100))
chute = ''
pontos_jogador = 1000
tentativas = 0
resposta = ''

while True:
    print(numero_secreto)
    input('Vamos começar? Aperte ENTER para iniciar: ')
    while not chute == numero_secreto:
        try:
            chute = int((input('Digite um número: ')))
            tentativas += 1

        except:
            print('Você deveria digitar um número entre 1 e 100...')
            continue

        if chute < 1 or chute > 100:
            print('Você deveria digitar um número entre 1 e 100...')
            continue

        if tentativas == 30:
            print('Você atingiu o limite de tentativas e perdeu o jogo :(')
            break

        if chute == numero_secreto:
            print(f'Parabéns, você acertou!'
                  f'\nO número secreto era {numero_secreto}.')
        elif chute > numero_secreto:
            print(f'Você errou, tente um número menor')

        elif chute < numero_secreto:
             print(f'Você errou, tente um número maior')

        else:
            print(f'amor')
    break


