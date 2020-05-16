'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
cuenta atrás desde ese número hasta cero separados por comas.
'''
#range(start_value, end_value, step)
#range(start_value, end_value,)
#range(end_value)

n = int(input('Introduce un número entero positivo: '))
for i in range(n, -1, -1):
    print(i, end= ', ')
