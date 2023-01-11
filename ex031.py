'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
distancia = int(input('De quantos Km será sua viagem? '))
d1 = distancia*0.50
d2 = distancia*0.45
if distancia <= 200:
    print('Sua viagem será de {} kms e o preço da sua passagem será R$ {:.2f}'.format(distancia, d1))
else:
    print('Sua viagem será de {} kms e o preço será R$ {:.2f}'.format(distancia, d2))
