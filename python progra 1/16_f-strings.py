# CADENAS DE CARACTERES
# f-strings (formatted strings)

# Variables
dia = 25
mes = "diciembre"
cad = f'Navidad es el {dia} de {mes}'
print(cad) # Navidad es el 25 de diciembre

# Expresiones
print(f'{23*2+12}') # 58
mes = "octubre"
print(f'{mes.upper()} tiene {len(mes)} letras') # OCTUBRE tiene 7 letras
print()

# Alineación de números y cadenas
num = 25
cad = f'|{num:5}|'
print(cad) # |   25|

num = 25
cad = f'|{num:05}|'
print(cad) # |00025|

num = 8
cad = f'|{num:<5}|'
print(cad) # |8    |
cad = f'|{num:>5}|'
print(cad) # |    8|
cad = f'|{num:^5}|'
print(cad) # |  8  |

texto = "Hola"
cad = f'|{texto:-^8}|'
print(cad) # |--Hola--|

pi = 3.1416
cad = f'{pi:.2f}'
print(cad) # 3.14