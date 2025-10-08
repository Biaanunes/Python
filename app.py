n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1>n2 and n1>n3:
    print(f'O maior número é {n1}')
elif n2>n1 and n2>n3:
    print(f'O mairo número é {n2}')
else:
    print(f'O maior número é {n3}')

#OU
primeiro = int(input('Digite um número: '))
segundo = int(input('Digite outro número: '))
terceiro = int(input('Digite o último número: '))

def maiorNumero():
    resposta = max(primeiro, segundo, terceiro)
    print(f'O maior número é {resposta}')
maiorNumero()

