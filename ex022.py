'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas [ok].
– Quantas letras ao todo (sem considerar espaços)[ok].
– Quantas letras tem o primeiro nome.[ok]'''

nome = str(input('Digite Seu Nome Completo: ')).strip()
# Fiz tua em uma única variável (n ficou agradavel, mas funcionou)
print('O seu nome com letras maiusculas fica {}'.format(nome.upper()))
print('O seu nome com letras minusculas fica {}'.format(nome.lower()))
# Fiz tua em uma única variável (n ficou agradavel, mas funcionou)
print('O seu nome tem ao todo o numero de {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))