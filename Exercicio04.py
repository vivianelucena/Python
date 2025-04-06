#   Entrada de 2 números e mostre a ordem crescente deles

n1 = float(input(f'Digite um número: '))
n2 = float(input(f'Digite um número: '))

if n1 > n2 :
    print(f'O valor {n1} é maior que {n2}!\nEm ordem crescente fica: {n2,n1}\n')
else:
    print(f'\nO valor {n2} é maior que {n1}!\nEm ordem crescente fica: {n1,n2}')
