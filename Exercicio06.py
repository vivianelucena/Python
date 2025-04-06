time1 = input(f'Digite o nome do primeiro time: ')
time2 = input(f'Digite o nome do primeiro time: ')

golTime1 = int(input(f'Digite quantos gols o time {time1} fez: '))
golTime2 = int(input(f'Digite quantos gols o time {time2} fez: '))

time01 = golTime1
time02 = golTime2

print(f'O {time1} fez {golTime1} gols!')
print(f'O {time2} fez {golTime2} gols!')


if time01 > time02:
    print(f'O time {time1} fez {golTime1} e ganhou!')

elif time01 == time02:
    print(f'O jogo deu empate!')

else:
    print(f'O time {time2} fez {golTime2} e ganhou!')