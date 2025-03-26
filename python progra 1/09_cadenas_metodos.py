# CADENAS DE CARACTERES
# Métodos comunes

# cadena.index(subcadena, [inicio], [fin])
print("Index:")
cadena = "Hola, mundo"
indice = cadena.index("mundo")
print(indice) # 6

# cadena.count(subcadena, [inicio], [fin])
print("\ncount:")
cadena = "Hola, hola, mundo. Hola a todos"
print(cadena.count("Hola")) # 2
print(cadena.count("hola")) # 1

# cadena.replace(subcadena_antigua, subcadena_nueva, [num_reemplazos])
print("\nreplace:")
cadena = "Hola mundo, el Mundo es grande."
nueva_cadena = cadena.replace("Mundo", "mundo")
print(nueva_cadena)  # Hola mundo, el mundo es grande.

# cadena.strip([caracteres]), cadena.lstrip([caracteres]), cadena.rstrip([caracteres])
print("\nstrip, lstrip y rstrip:")
cadena = "  Hola, mundo!  "
limpia = cadena.strip()
print(limpia) # "Hola, mundo!"

cadena = "  Hola, mundo!  "
limpia = cadena.lstrip()
print(limpia) # "Hola, mundo!  "

cadena = "  Hola, mundo!  "
limpia = cadena.rstrip()
print(limpia) # "  Hola, mundo!"

cadena = "++Hola, mundo!--"
limpia = cadena.strip("+-!")
print(limpia)  # "Hola, mundo"

# cadena.center(ancho, [relleno])
# cadena.ljust(ancho, [relleno])
# cadena.rjust(ancho, [relleno])
print("\ncenter, ljust y rjust:")
cadena = "Python"
print(cadena.center(20, '*')) # *******Python*******
print(cadena.ljust(20, '-')) # Python--------------
print(cadena.rjust(20, '+')) # ++++++++++++++Python

print("\nzfill:")
# cadena.zfill(ancho)
n = 25
cad = str(n).zfill(6)
print(cad) # 000025