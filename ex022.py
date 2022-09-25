'''Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas [ok].
– Quantas letras ao todo (sem considerar espaços)[ok].
– Quantas letras tem o primeiro nome.[ok]'''

nome = str(input('Digite Seu Nome Completo: '))
# Fiz tua em uma única variável (n ficou agradavel, mas funcionou)
maiusculas = (nome.upper()) , (nome.lower())

# Removi espaços de ANTES e depois do nome
numero = len(nome.strip())

# separei variavel em lista (split)
lista = nome.split()
primeiro = len(lista[0]) #criei uma nova variavel  puxando o LEN e a posição da variavel

print(maiusculas)
print(numero)
print(primeiro)
