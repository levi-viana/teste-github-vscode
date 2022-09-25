'''faça um algoritmo que leia um preço de um produto e mostre seu novo preço com 5% de desconto'''
p = float(input('Digite o Preço: '))
d = (p*0.05)
pf = (p-d)
print('O o novo preço com o desconto ficou {}'.format(pf))
