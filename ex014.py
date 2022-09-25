''' Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''
temp = int(input('Temperatura em Celsius: '))
faren = (temp * 9/5) + 32
print('{} graus celsius conrresponde á {} Fahrenheit'.format(temp, faren))
