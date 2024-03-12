import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contrasena = int(input("Ingresa la longitud de la contraseña que deseas generar: "))
nueva_contrasena = generar_contrasena(longitud_contrasena)
print("Tu nueva contraseña aleatoria es:", nueva_contrasena)

