valor1 = float(input(f'Digite o primeiro valor: '))
valor2 = float(input(f'Digite o segundo valor: '))

adicao = valor1 + valor2
subtracao = valor1 - valor2
divisao = valor1 / valor2
multiplicacao = valor1 * valor2

print(f'O valor um é: {valor1} \nO valor dois é: {valor2}')
print(f'\n{valor1} + {valor2} = {adicao:.2f}')
print(f'\n{valor1} - {valor2} = {subtracao:.2f}')
print(f'\n{valor1} / {valor2} = {divisao:.2f}')
print(f'\n{valor1} * {valor2} = {multiplicacao:.2f}')