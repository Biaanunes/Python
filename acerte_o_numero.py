import random
numero_certo = random.randint(1, 10)
chute = int(input('Digite um número: '))

while chute != numero_certo:
    if chute < numero_certo:
        print('\nO número é maior\n')
    elif chute > numero_certo:
        print('\nO número é menor\n')
    chute = int(input('Digite um número: '))

print('\nVocê acertou o número secreto!\n')
