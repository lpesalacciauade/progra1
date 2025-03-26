# CADENAS DE CARACTERES
# Algunos ejemplos

# Invertir una cadena por letra
cadena = "Programación I"
cadena_invertida = cadena[::-1]
print(cadena_invertida) # I nóicamargorP

# Invertir una frase por palabra
frase = input("Ingrese una frase: ")
palabras = frase.split() # Partimos la frase en una lista de palabras
palabras.reverse() # Invertimos la lista con reverse
frase = ' '.join(palabras) # Construimos la cadena a partir de la lista
print(frase)
# Resultado:
# Ingrese una frase: Hola cómo estás
# estás cómo Hola