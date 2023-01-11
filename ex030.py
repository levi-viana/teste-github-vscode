'''Crie um programa que leia um número inteiro e mostre na
 tela se ele é PAR ou ÍMPAR.'''
numero = int(input('Digite um numero: '))
resultado = numero % 2 #macete matematico para divisão e restante
if resultado == 0:
    print('O número escolhido é PAR')
else:
    print('O número escolhido é IMPAR')

