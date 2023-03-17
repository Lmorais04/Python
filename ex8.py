nome=input('nome do vendendedor:')
carros_vendidos=int(input(' carros vendidos:'))
valor=float(input('valor total das vendar:"'))
comissão= 200*carros_vendidos
acrescimo= valor*2/100
salario= 2500+comissão+acrescimo
print(f'salario do vendedor {nome} é {salario}')

