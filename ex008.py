'''escreva um programa que leia um valor em metros e o exiba em centimetros e milimetros'''
m = float(input('Digite um valor em metros: '))
centimetro = (m*100)
milimetros = (m*1000)
print('O valor de metros convertido em centimetros é {:.0f}'.format(centimetro))
print('O valor de metros convertido em milimetros é {:.0f}'.format(milimetros))

