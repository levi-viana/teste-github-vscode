'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
 triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''
 
import math
catetooposto = float(input('Digite o comprimento do Cateto Oposto: '))
catetoadjacente = float(input('Digite o comprimento do Adjacente: '))
hipotenusa = math.hypot(catetooposto, catetoadjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
