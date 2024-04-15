valor1= True or False and False # Devuelve True
valor2= True or False or False # Devuelve True
valor3= True and True and False # Devuelve False

valor1_modificado = (True or False) and False  # Devuelve False
valor2_modificado= True or (False or False) # Devuelve True
valor3_modificado= True and (True and False) # Devuelve False

print('Valores sin modificar precedencias')
print(f'Valor1: {valor1}')
print(f'Valor2: {valor2}')
print(f'Valor3: {valor3}')

print('Valores modificando precedencias')
print(f'Valor1: {valor1_modificado}')
print(f'Valor2: {valor2_modificado}')
print(f'Valor3: {valor3_modificado}')

