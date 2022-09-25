'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
 cosseno e tangente desse ângulo'''
import math
ang = float(input('Digite o Angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('Com um angulo de {}, o seu seno é de {:.1f}, cosseno {:.1f} e tangente {:.1f}'.format(ang, sen, cos, tangente))

'''ou usar FROM MATH IMPORT SIN, COS, TAN, RADIANS'''