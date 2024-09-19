print ("Hola Mundo")

#Inicializar un valor
valor = 3
print(valor)

import keyword
#Todas las palabras restringidas
print(keyword.kwlist)

#Comprobar si la palabra es restringida
print(keyword.iskeyword('pass'))
print(keyword.iskeyword('variable'))

#Ver todos los modulos posibles
help('modules')

edad = 24
nombre = 'Maria'
print('La edad de ',nombre, ' es ', edad)

semanas = 4
print('En',semanas, 'semanas hay', 7*semanas,'dias')

#Para que no deje los espacios
print(f'¡Hola {nombre}!')

#Escribir el nombre por teclado 
#Primera forma
print('¿Como te llamas?')
nombre = input()
print('Hola',nombre)

#Segunda forma
nombre = input('¿Como te llamas?')
print('Hola',nombre)

#Hacer un división y que te de el resto y el cociente
print(divmod(13,4))

#Para redondear un número 
n=2/5*3

#Aqui te quita los decimales
print(round(n))

#Aqui deja dos decimales
print(round(n,2))

#La funcion math

import math

print(math.floor(5.2))
print(math.ceil(5.2))

#Hacer el valor absoluto de un número
print(abs(-2))

#Pasar el valor maximo
max(2,4,8)



#Booleanos

a = True

#Contradiccion
print (not a)

#Condicionales
edad = 17

if (edad > 18 and edad < 65):
    print('Es mayor de edad')
elif (edad >=65):
    print('Es jubilado')
else:
    print ('Es menor de edad')

#Funciones

def hola():
    print('Hola mundo')

hola()

#Funciones con parametros

def division(x,y):
    q = x//y
    r=x%y
    return (q,r)

print(division(x=4,y=2))
