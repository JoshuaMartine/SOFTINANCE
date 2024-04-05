from customtkinter import *
from tkinter import PhotoImage
from PIL import Image
import subprocess
import os

colorGris = "#323232"
azul = "#00c4cc"
negro = "#000000"

root = CTk()
root.title("ROSSE AI")
root.resizable(False, False)
root.configure(background="black")
root.iconbitmap("a.ico")

set_appearance_mode( " dark " )

# Función para centrar la ventana en la pantalla
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
# Configurar la ventana en el centro
window_width = 1000
window_height = 600
center_window(root, window_width, window_height)

       
def on_enter(event):
    iniciarSesionBB.configure(text_color=azul) 

def on_leave(event):
    iniciarSesionBB.configure(text_color="white") 
    
def login():
    archivo_a_ejecutar = "login.py"
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(directorio_actual, archivo_a_ejecutar)
    os.system(f"python {ruta_completa}")
    root.destroy()
        
#fondo del las opciones de inicio de sesion
frame = CTkFrame(root, width=500, height=745, fg_color=negro)
frame.place(x=500, y=0)

#titulo del inicio de sesion
titulo = CTkLabel(root,text="Bienvenido!", bg_color=negro, font=("Arial black",30), text_color=azul)
titulo.place(x=520,y=80)

#descripcion
subText = CTkLabel(root, text="Rellena los campos para registrarte", font=("Helvetica bold",20), bg_color=negro, text_color="white")
subText.place(x=520, y=120)

#correo
tituloCorreo = CTkLabel(root, text="Correo", font=("Helvetica bold",20), bg_color=negro, text_color="white")
tituloCorreo.place(x=545, y=180)

correo = CTkEntry(root, font=("sans serif", 16), bg_color="black",  border_color=azul, fg_color=negro, width=380, height=40, corner_radius=15)
correo.place(x=520, y=210)

#contraseña
tituloContraseña = CTkLabel(root, text="Contraseña", show="*", font=("Helvetica bold",20), bg_color=negro, text_color="white")
tituloContraseña.place(x=545, y=280)

contraseña = CTkEntry(root, font=("sans serif", 16), border_color=azul, fg_color=negro, width=380, bg_color="black", height=40, corner_radius=15)
contraseña.place(x=520, y=310)

#Repetir contraseña
rTituloContraseña = CTkLabel(root, text="Confirmar contraseña", font=("Helvetica bold",20), bg_color=negro, text_color="white")
rTituloContraseña.place(x=545, y=380)

rContraseña = CTkEntry(root, font=("sans serif", 16), border_color=azul, fg_color=negro, width=380, bg_color="black", height=40, corner_radius=15)
rContraseña.place(x=520, y=410)

#boton de inicio de sesion
registrarseB = CTkButton(root, text="Registrarse", fg_color=azul, border_color=azul, text_color=negro, bg_color="black",
                           width=380, height=40, cursor="hand2", font=("Arial Rounded MT bold",25), corner_radius=15)
registrarseB.place(x=520, y=490)

#boton registrase
iniciarSesionBB = CTkLabel(root, text="¿Ya tienes una cuenta? Inicia sesión aquí", font=("Helvetica bold",12),
                        bg_color=negro, cursor="hand2", text_color="white")
iniciarSesionBB.place(x=590, y=530)

iniciarSesionBB.bind("<Enter>", on_enter)  
iniciarSesionBB.bind("<Leave>", on_leave)
iniciarSesionBB.bind("<Button-1>", lambda event: login())

# Cargar imagen
imagen = PhotoImage(file="a.png")
imagen = imagen.subsample(15,15)  

mailLogo = PhotoImage(file="email.png")
mailLogo = mailLogo.subsample(25,25)

passLogo = PhotoImage(file="bloquear.png")
passLogo = passLogo.subsample(25,25)

rose = PhotoImage(file="rose.png")


# Mostrar imagen en la interfaz gráfica

imagen_label1 = CTkLabel(root, image=mailLogo, text="", bg_color=negro)
imagen_label1.place(x=520, y=180)

imagen_label3 = CTkLabel(root, image=rose, text="", bg_color=negro)
imagen_label3.place(x=0, y=0)

imagen_label = CTkLabel(root, image=imagen, text="", bg_color="black")
imagen_label.place(x=20, y=20)

imagen_label2 = CTkLabel(root, image=passLogo, text="", bg_color=negro)
imagen_label2.place(x=520, y=280)

imagen_label2 = CTkLabel(root, image=passLogo, text="", bg_color=negro)
imagen_label2.place(x=520, y=380)

#texto del logo
nombreLogo = CTkLabel(root, text="ROSSE", text_color=azul, bg_color="black", font=("Audiowide", 15))
nombreLogo.place(x=70, y=30)
root.mainloop()