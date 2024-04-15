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


recreo = 0

while (recreo <= 15):

    if(recreo == 15):
        print('Chicos fin del recreo!!')
    
    if(recreo == 0):
        print('Chicos todos al recreo!')
    
    if((recreo > 0) and (recreo < 15)):
        print(f'Los chicos llevan {recreo} minutos')
        print('Esperamos un minuto más...')
    
    recreo += 1


manzanas = ['manzana roja', 'manzana verde', 'manzana roja arenosa', 'manzana roja deliciosa', 'manzana verde ácida']

for manzana in manzanas:
    print(f'Ahora estoy comiendo una {manzana}')

print('Ingresá 10 números y te contamos cuántos divisores tiene cada uno')

for n in range(10):
    num = int(input('Ingresá un número entero positivo: '))

    while num <= 0:
        num=int(input('Ingresá un número entero positivo: '))
    
    cant_divisores = 0
    
    for d in range(2,num//2+1):
        if num % d == 0:
            cant_divisores += 1
    print(num,'tiene',cant_divisores,'divisores')