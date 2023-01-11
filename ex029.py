'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

v = int(input('Qual a velocidade do carro ? '))
velo = (v-80)
multa = (velo*7)
if v >= 80:
    print('Você foi multado, ultrapassou {} km/hr acima do limite e sua multa foi de R$ {}'.format(velo, multa))
else:
    print('Passou limpo, continue dirigindo com segurança!')

# fiz o input e logo em seguida fiz as condições (basicas) so levando em consideração se levaria multa ou n
# Depois fiz 2 variaveis: 1 pra calcular input menos 80 que daria o restante (KM) e 1 pra multa resto*7
