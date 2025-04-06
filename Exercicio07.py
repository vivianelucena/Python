combustivel = input(f'Qual o tipo de combustível?\n G - Gasolina\n E - Etanol\n')

litros = float(input(f'Quantos litros foi colocado?'))

if combustivel == 'G' or combustivel == 'g' :
    valor = litros*5.8

elif combustivel == 'E' or combustivel == 'e' :
    valor = litros*4.9
else:
    print('Tipo de combustível inválido!')

print(f'Você colocou {litros}L, o valor total a ser pago será: {valor:.2f}!')