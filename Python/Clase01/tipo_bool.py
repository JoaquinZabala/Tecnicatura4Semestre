
#Bool contiene los valores de True y False
#Los tipos numéricos, es false para el 0 (cero), true para los demás valores
valor = 0
resultado = (bool(valor)
print(f'valor: {valor}, Resultado); {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'valor:{valor}, Resultado: {resultado}')

#Tipo string -> False '', True demás valores
valor = ''
resultado = (bool(valor)
print(f'valor: {valor}, Resultado); {resultado}')

valor = 'Hola'
resultado = (bool(valor)
print(f'valor: {valor}, Resultado); {resultado}')

  #Tipo colecciones -> -False para colecciones vacias
#Tipo colecciones -> True para todos las demás
#Lista
valor = []
resultado = bool(valores)
print(f'valor:{valor}, Resultado: {resultado}')

valor = []
resultado = bool(valores)
print(f'valor:{valor}, Resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'valor de una tupla vacia: {valor}, Resultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'valor de una tupla con elemento: {valor}, Resultado: {resultado}')

#Diccionario
valor = {}
resultado = bool(valor)
print(f'valor de un diccionario vacio: {valor}, Resultado: {resultado}')

valor = {'Nombre':'Juan','Apellido':'Perez'}
resultado = bool(valor)
print(f'valor de un diccionario con elemento: {valor}, Resultado: {resultado}')

#Sentencias de control con bool
if(1,)
print('Regresa verdadero')
else:
print('Regresa falso')

#Ciclos
variable = 17
while variable:
    print('Regrese verdadero')
    break
else:
    print('Regresa falso')
