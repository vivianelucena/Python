min01 = 45
min02 = 20

minutos = min01 + min02
minutofinal = minutos - 60

hora01 = 3
hora02 = 14
hora = (hora01 + hora02) + 24
hora1 = hora/2

if minutos > 59:
    hora1+=1
    #minutosfinal - 6
    print(f'{hora1}:{minutofinal}')
else:
    minutos - 60
    print(f'{hora1}:{minutos}')