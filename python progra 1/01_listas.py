# LISTAS
# Creación, acceso a elementos y actualización de valores
print("Creación, acceso a elementos y actualización de valores:")
frutas = ["manzana", "banana", "cereza", "durazno"]
print(frutas[0]) # manzana
print(frutas[2]) # cereza
print(frutas[-1]) # durazno
frutas[1] = "naranja"
print(frutas) # ['manzana', 'naranja', 'cereza', 'durazno']
# print(frutas[4]) # IndexError: list index out of range
print(frutas[len(frutas)-1]) # último elemento: durazno
print(frutas[-1]) # durazno
print(frutas[-len(frutas)]) # manzana
print()

# Otros ejemplos de listas
print("Otros ejemplos de listas:")
listaNumeros = [1,2,3,4]
listaTexto = ["Hola", "Mundo", "!"]
listaDistintosTipos = ["A", True, 123, 123.12]
listaDeListas = [ [1,2,3], [4,5,6] ]
listaVacia = [ ] # También puede usarse list()
lista = [ ]
for i in range(4):
    lista.append(i**2) # Resultado: [0, 1, 4, 9]
print()

print("Impresión de listas con for y while:")
# Impresión de listas con for y while
for i in range(len(lista)):
    print(lista[i], end=' ')
print()
# Resultado: 0 1 4 9 

pos = 0
while pos < len(lista):
    print(lista[pos], end=' ')
    pos += 1
print()
# Resultado: 0 1 4 9

# También es posible iterar una lista utilizando el operador in
for valor in lista:
    print(valor, end=" ")
# Resultado: 0 1 4 9


# Listas por comprensión

# Forma de crear una lista tradicional
numeros = [0,1,2,3,4,5]
cuadrados = []
for num in numeros:
    cuadrados.append(num**2)
print("Lista tradicional:", cuadrados)
# [0, 1, 4, 9, 16, 25]

# A través de listas por comprensión
numeros = [0,1,2,3,4,5]
cubos = [num**3 for num in numeros]
print("Lista por comprensión:", cubos) # [0, 1, 8, 27, 64, 125]

# Es posible filtrar elementos, incorporando if / if-else
lista = [1,-2,5,0,3,4]
listaCuadradosParesPorComp = [num**2 for num in lista if num%2==0]
print("Lista filtrada:", listaCuadradosParesPorComp) # [4, 0, 16]

# Elevo al cuadrado los pares y los impares quedan igual
lista = [1,-2,5,0,3,4]
listaPorComp = [num**2 if num%2==0 else num for num in lista]
print("lista modificada:", listaPorComp) # [1, 4, 5, 0, 3, 16]
