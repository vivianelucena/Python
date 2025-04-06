nota1 = float(input(f'Digite a primeira nota: '))
nota2 = float(input(f'Digite a segunda nota: '))
nota3 = float(input(f'Digite a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if media>=7 :
    print(f'Aluno aprovado! A média dele foi: {media:.2f}!')

elif media<4:   #else: if media <4 :
    print(f'Aluno reprovado! A média dele foi: {media:.2f}!')

else:
    print(f'Aluno em recuperação! A média dele foi: {media:.2f}!')