'''Crie um programa que leie um salário de um funcionário e mostre seu novo valor com aumento de 15%'''
salario = float(input('Digite aqui o seu salário: '))
aumento = (salario*0.15)
salariofinal = (salario+aumento)
print('O seu novo salário com o aumento ficou de R$ {}'.format(salariofinal))