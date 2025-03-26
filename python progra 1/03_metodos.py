
# LISTAS
# Métodos integrados

# a. Métodos para agregar elementos
print("a. Métodos para agregar elementos:")
nombres = ["María", "Luis", "Diego"]
nombres.append("Luciana")
print(nombres) # ['María', 'Luis', 'Diego', 'Luciana']

numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(numeros) # [1, 2, 3, 4, 5, 6]

estaciones = ["Verano", "Otoño", "Primavera"]
estaciones.insert(2, "Invierno")
print(estaciones) # ['Verano', 'Otoño', 'Invierno', 'Primavera']

# Si no existe la posición lo agrega al final
colores = ["Verde", "Rojo", "Azul"]
colores.insert(4, "Naranja")
print(colores) # ['Verde', 'Rojo', 'Azul', 'Naranja']
print()

# b. Métodos para quitar elementos
print("b. Métodos para quitar elementos:")
estaciones = ["Verano", "Otoño", "Invierno", "Primavera"]
estaciones.remove("Otoño")
print(estaciones) # ['Verano', 'Invierno', 'Primavera']

colores = ["Rojo", "Azul", "Verde", "Naranja"]
color_eliminado = colores.pop()
print("Color eliminado:", color_eliminado) # Color eliminado: Naranja
print(colores) # ['Rojo', 'Azul', 'Verde']

meses = ["Abril", "Mayo", "Junio", "Julio"]
mes_eliminado = meses.pop(2)
print("Mes eliminado:", mes_eliminado) # Mes eliminado: Junio
print(meses) # ['Abril', 'Mayo', 'Julio']

nombres = ["María", "Luis", "Diego"]
nombres.clear()
print(nombres) # []
print()

print("c. Otros métodos:")
vocales = ['a','e','i','o','u']
pos_i = vocales.index('i')
print("Posición de i:", pos_i) # Posición de i: 2

nombres = ["Ana", "Luis", "Pedro", "Ana", "Carlos", "Ana", "Luis"]
cantidad_ana = nombres.count("Ana")
print("Apariciones de 'Ana':", cantidad_ana) # Apariciones de 'Ana': 3
print()

print("d. Métodos para invertir el orden:")
numeros = [4, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros) # [1, 2, 4, 5, 6, 9]
numeros.sort(reverse=True)
print(numeros) # [9, 6, 5, 4, 2, 1]
numeros.sort(key=lambda x:x%2) # primero pares, luego impares
print(numeros) # [6, 4, 2, 9, 5, 1]

vocales = ['a','e','i','o','u']
vocales.reverse()
print(vocales) # ['u', 'o', 'i', 'e', 'a']



# Funciones de listas

print("Funciones en listas:")
numeros = [5, 3, 8, 6, 2, 7, 4, 1]
largo = len(numeros)
print("Largo de la lista:", largo) # Largo de la lista: 8
suma_total = sum(numeros)
print("Suma:", suma_total) # Suma: 36
valor_minimo = min(numeros)
print("Valor mínimo:", valor_minimo) # Valor mínimo: 1
valor_maximo = max(numeros)
print("Valor máximo:", valor_maximo) # Valor máximo: 8
cadena_vocales = "aeiou"
lista_vocales = list(cadena_vocales)
print(lista_vocales) # ['a', 'e', 'i', 'o', 'u']



# Operaciones


# Concatenación
print("Concatenación:")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print(lista_concatenada) # [1, 2, 3, 4, 5, 6]
print()

# Copia
print("Copia:")
lista_original = [1, 2, 3]
print("Original:", lista_original, id(lista_original)) 
lista_copia = lista_original.copy()
print("Copia 1:", lista_copia, id(lista_copia)) 
lista_copia2 = lista_original[:]
print("Copia 2:", lista_copia2, id(lista_copia2)) 
lista_copia3 = list(lista_original)
print("Copia 3:", lista_copia3, id(lista_copia3)) 
print()

# Multiplicación
print("Multiplicación:")
listaNumeros = [1,2,3,4]
listaNumeros = listaNumeros * 2
print(listaNumeros) # [1, 2, 3, 4, 1, 2, 3, 4]
print()

# Pertenencia
print("Pertenencia:")
listaNumeros = [1,2,3,4]
print(4 in listaNumeros) # True
print(3 not in listaNumeros) # False
print()

# Desempaquetado
print("Desempaquetado:")
listaNumeros = [1,2,3,4]
num1, num2, num3, num4 = listaNumeros
print(num1) # 1
print(num2) # 2
print(num3) # 3
print(num4) # 4