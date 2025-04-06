          #entrada01 =  3.45
          #entrada02 = 14.20
          #saida = 6.05

#   Entrada das horas e minutos
hora01 = 3
min01 = 45

hora02 = 14
min02 = 20


#   Somando os minutos
minutos = min01 + min02

#   Minutos para minutos > 59
minutofinal = minutos - 60


hora = hora01 + hora02
horafinal = hora - 12   #   Para o resultado ser no formato am pm



#   Para quando a soma dos minutos da mais que 60
if minutos > 59:
    horafinal += 1
    minutofinal
    print(f'{horafinal}h{minutofinal:02}')
else:
    minutos - 60
    print(f'{horafinal}h{minutofinal:02}')


#OBS.: Ainda está com erro, quando o resultado é ser no formato 12h está dando 24h e vice-versa