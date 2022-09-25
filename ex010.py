'''crie um programa que leia o quanto a pessoa tem na carteira e mostre quantos dolares ela pode comprar'''
v = int(input('Digite o valor que você tem: '))
dolar = (v/5.16)
print('Com o valor que você tem, poderá comprar {:.0f} dolares!'.format(dolar))