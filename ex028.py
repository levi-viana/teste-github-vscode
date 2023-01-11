''' Escreva um programa que faça o computador “pensar” em um número 
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
 escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
n = int(input('Digite um número de 0 a 5: '))
x = random.randint(1, 5)
print('O numéro sorteado foi {} e você escolheu {}'.format(x, n))
if n == x:
    print('Você acertou! Parabens!')
else:
    print('Você errou, tente novamete')

# Fiz o programa por partes, busquei o input do usuário
# Depois pesquisei a biblioteca random e usei a função randit
# Organizei as condições iF e else dependendo do resultado.