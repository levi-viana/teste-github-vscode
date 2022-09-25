''' Um professor quer sortear um dos seus 3 alunos para apagar o quadro.
 Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''
import random
a1 = str(input('Nome do Aluno 1: '))
a2 = str(input('Nome do Aluno 2: '))
a3 = str(input('Noem do Aluno 3: '))
lista = [a1, a2, a3]
escolhido = random.choice(lista)
print('O Aluno escolhido para apagar o quadro foi o {}'.format(escolhido))
