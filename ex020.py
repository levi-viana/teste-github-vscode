''' O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.'''
from random import shuffle
a1 = str(input('Nome do Aluno 1: '))
a2 = str(input('Nome do Aluno 2: '))
a3 = str(input('Nome do Aluno 3: '))
a4 = str(input('Nome do ALuno 4: '))
lista = [a1, a2, a3, a4]
ordem = shuffle(lista)
print('A ordem de apresentação de acordo com os nomes ficará {}'.format(lista))
