'''Faça um programa que leia a largura e altura de uma parede em metros, calcule a área e a quantidade 
de tinta necessária para pinta-la. Sabendo que cada litro pinta uma área de 2m quadrados'''
altura = float(input('Qual a altura da parede (metros) ?: '))
largura = float(input('Qual a largura da parede (metros) '))
area = (altura*largura)
tinta = (area/2)
print('A área da parede é equivalente a {:.0f}m², e será preciso de {:.0f}L de tinta'.format(area, tinta))

