# dar formato a un string

nombre = 'Nicolas'
edad = 38
mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)  # %s (s=string) apunta a la variable string
# %d (d=decimal) apunta a la variable decimal
# creamos una tupla                                                    # se comporta igual que una tupla
print(mensaje_con_formato)
persona = ('Carla', 'Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s .Tus sueldo es %.2f'  # %persona aquí se le pasa el objeto tupla

print(mensaje_con_formato % persona)

nombre = 'Pedro'
edad = 38
sueldo = 3000
# mensaje_con_formato = 'Nombre {} edad {} sueldo {:.2f}'.format(nombre, edad, sueldo)
# print(mensaje_con_formato)

# mensaje = 'Nombre {0} edad {1} sueldo {2:.2f}'.format(nombre, edad, sueldo) # trabajo con índices
# print(mensaje)

mensaje = 'Nombre {n} edad {e} sueldo{s:.2f}'.format(n=nombre, e=edad, s=sueldo)
# print(mensaje)

diccionario = {'nombre': 'Nicolás', 'edad': 38, 'sueldo': 8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo{dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)
