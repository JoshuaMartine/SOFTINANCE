from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry, CTkCheckBox, CTkImage
from tkinter import PhotoImage
from PIL import Image

colorGris = "#323232"
azul = "#00c4cc"
negro = "#000000"

root = CTk()
root.title("ROSSE AI")
root.geometry("1366x685+0+0")
root.minsize(480,500)

def on_enter():
        registrarseB.config(text_color=azul)
def on_leave():
        registrarseB.config(text_color="black")
        

# Cargar imagen
imagen1 = PhotoImage(file="b.png")
imagen1 = imagen1.subsample(1,1)  # Redimensionar la imagen

# Mostrar imagen en la interfaz gráfica
imagen_label = CTkLabel(root, image=imagen1, text="", bg_color=negro)
imagen_label.place(x=500, y=0)
    
#fondo del las opciones de inicio de sesion
frame = CTkFrame(root, width=500, height=745, fg_color=negro)
frame.place(x=0, y=0)

#titulo del inicio de sesion
titulo = CTkLabel(root,text="Iniciar Sesión", bg_color=negro, font=("Arial Rounded MT bold",50))
titulo.place(x=20,y=160)

#texto del logo
nombreLogo = CTkLabel(root,text="ROSSE", text_color=azul, bg_color=negro, font=("Audiowide",15))
nombreLogo.place(x=80,y=30)

#correo
tituloCorreo = CTkLabel(root, text="Correo", font=("Helvetica bold",20), bg_color=negro)
tituloCorreo.place(x=20, y=270)

correo = CTkEntry(root, font=("sans serif", 12), placeholder_text="  Correo electronico", 
                  border_color="grey", fg_color=negro, width=450, height=60)
correo.place(x=20, y=300)

#contraseña
tituloContraseña = CTkLabel(root, text="contraseña", font=("Helvetica bold",20), bg_color=negro)
tituloContraseña.place(x=20, y=370)

contraseña = CTkEntry(root, font=("sans serif", 12), placeholder_text="  Contraseña ", 
                  border_color="grey", fg_color=negro, width=450, height=60)
contraseña.place(x=20, y=400)

#boton de inicio de sesion
iniciarSesionB = CTkButton(root, text="Iniciar sesion", fg_color=azul, border_color=azul, text_color=negro,
                           width=450, height=60, cursor="hand2")
iniciarSesionB.place(x=20, y=490)

#boton registrase
registrarseB = CTkLabel(root, text="¿No tienes cuenta? registrate aquí", font=("Helvetica bold",20),
                        bg_color=negro, cursor="hand2")
registrarseB.place(x=20, y=650)

registrarseB.bind("<Enter>", on_enter)
registrarseB.bind("<Leave>", on_leave)


# Cargar imagen
imagen = PhotoImage(file="a.png")
imagen = imagen.subsample(15,15)  # Redimensionar la imagen

# Mostrar imagen en la interfaz gráfica
imagen_label = CTkLabel(root, image=imagen, text="", bg_color=negro)
imagen_label.place(x=20, y=20)




root.mainloop()