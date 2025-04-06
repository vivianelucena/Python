#  Salário e pocentual de aumento

nome = input(f'Digite seu nome: ')

idade = int(input(f'Digite sua idade: '))

salario = float(input(f'Digite seu salário: '))

aumento = float(input(f'Digite a porcentagem do aumento: '))

print(f'\nNome: {nome} \nIdade: {idade} \nSalário: {salario:.2f}')

porcentagem = (salario*aumento)/100

salarioAtual = salario + porcentagem

#   :.2f  -> mostra duas casas decimais

print(f'\nNome: {nome} \nIdade: {idade} \nNovo salário: {salarioAtual:.2f}')


