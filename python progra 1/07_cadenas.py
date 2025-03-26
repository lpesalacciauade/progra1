# CADENAS DE CARACTERES

print("Cadenas de caracteres")
cadena1 = "Programación I"
cadena2 = 'P1'
frase1 = 'Me dijo "en minutos llega Laura" y finalmente nunca vino.'
# Una constante de cadena extensa puede ser
# distribuida en varias líneas con barra invertida
frase2 = 'Me dijo "en minutos llega Laura" ' \
        'y finalmente nunca vino.'
print(cadena1) # Programación I
print(cadena2) # P1
print(frase1) # Me dijo "en minutos llega Laura" y finalmente nunca vino.
print(frase2) # Me dijo "en minutos llega Laura" y finalmente nunca vino.

# Acceso por índice / longitud de la cadena
print(cadena1[0])
print(cadena2[1])
print("Largo de la cadena:", len(cadena1))
print()

# Operaciones
# - Concatenación (+)
# - Multiplicación (*)
# - Adición (+=)
# - Pertenencia (in)
# - Identificación (is)
# - Copia
# - Comparación

print("Operaciones: ")
cadena = "Hola" + "Mundo"
print("Concatenación:", cadena) # HolaMundo

print("Multiplicación:", cadena*2) # HolaMundoHolaMundo

cadena += "!"
print("Adición:", cadena) # HolaMundo!

print("Pertenencia:")
print("Hola" in cadena) # True
print("hola" in cadena) # False

print("Identificación:")
cadena2 = "HolaMundo!"
print(cadena is cadena2) # False
print(id(cadena), id(cadena2)) # No apuntan al mismo objeto en memoria
cadena3 = cadena
print(cadena is cadena3) # True
print(id(cadena), id(cadena3)) # Apuntan al mismo objeto en memoria
print()

print("Copia:")
copia_cadena = cadena
print(copia_cadena)  # "HolaMundo!"
# Aunque la cadena original y la copia tengan el mismo contenido, son independientes en su uso.
cadena = "Adiós, mundo"
print(cadena)  # "Adiós, mundo"
print(copia_cadena)  # "HolaMundo!"

print("Comparación:")
saludo1 = "Hola"
saludo2 = "Hola"
print(saludo1 == saludo2)  # True
saludo2 = "hola"
print(saludo1 == saludo2)  # False



# CADENAS DE CARACTERES
# Índices y subcadenas

# cadena = "hola, mundo"
# cadena[0] = "H" # TypeError: 'str' object does not support item assignment

print("Extracción de sub-cadenas (slicing):")
cadena = "Hola, mundo"
subcadena1 = cadena[:5]
print(subcadena1) # "Hola,"
subcadena2 = cadena[1:4]
print(subcadena2) # "ola"
subcadena3 = cadena[6:]
print(subcadena3) # "mundo"
subcadena4 = cadena[::3]
print(subcadena4) # "Hamd"
print()

# Funciones
print("Funciones:")
cadena = "HolaMundo"
print(len(cadena)) # 9
print(max(cadena)) # u
print(min(cadena)) # H
print()

# Pertenencia
print("Pertenencia:")
cad = "Martes"
if "te" in cad:
    print("se encuentra")
else:
    print("no se encuentra")
if "ié" not in cad:
    print("no se encuentra")
else:
    print("se encuentra")
print()

# Iteramos una cadena
print("Iteramos una cadena:")
cad = "Hoy es Lunes"
for letra in cad:
    print(letra, end=".") # H.o.y. .e.s. .L.u.n.e.s.