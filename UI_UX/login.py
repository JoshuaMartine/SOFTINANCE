# login.py
from tkinter import messagebox

def validar_credenciales(correo, contraseña):
    if correo == "juan@" and contraseña == "mami":
        mostrar_alerta_exito()
    else:
        mostrar_alerta_fallo()

def mostrar_alerta_exito():
    messagebox.showinfo("Éxito", "Inicio de sesión exitoso!")

def mostrar_alerta_fallo():
    messagebox.showerror("Error", "Inicio de sesión fallido. Por favor, introduzca el usuario y contraseña correctos.")


