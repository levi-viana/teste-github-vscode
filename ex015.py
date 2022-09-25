''' Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de 
dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
 e R$0,15 por Km rodado.'''
km = int(input('Quantos kms o carro percorreu? '))
dias = int(input('Quantidade de dias ele foi alugado? '))
valorkm = (km*0.15)
valordia = (dias*60)
total = (valorkm+valordia)
print('O valor a ser pago pelo aluguel do carro será de R$ {}.'.format(total))
