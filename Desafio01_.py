#entrada01 =  3.45
#entrada02 = 14.20
#saida = 6.05

hora01 = 3
hora02 = 14

min01 = 45
min02 = 20

minutos = min01 + min02
minutofinal = minutos - 60


hora01_convert = hora01 * 60 + min01
hora02_convert = hora02 * 60 + min02

hora = hora01 + hora02
hora1 = hora - 12

if minutos > 59:
    hora1+=1
    #minutosfinal - 6
    print(f'{hora1}:0{minutofinal}')
else:
    minutos - 60
    print(f'{hora1}:{minutos}')