numero=int(input('numero 3 digitos: '))

a=numero//100
resto= numero %100
b=resto//10
c=resto %10
print(f'numero invertido: {c} {b} {a}')