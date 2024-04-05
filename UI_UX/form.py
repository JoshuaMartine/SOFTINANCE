# gui.py
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry
import login

colorGris = "#323232"
azul = "#00c4cc"
negro = "#000000"

def iniciar_sesion():
    correo_value = correo_entry.get()
    contraseña_value = contraseña_entry.get()
    login.validar_credenciales(correo_value, contraseña_value)

    
root = CTk()
root.title("ROSSE AI")
root.geometry("1366x685+0+0")
root.minsize(480,500)
root.config(bg="white")

def on_enter(event):
    registrarseB.config(text_color=azul)

def on_leave(event):
    registrarseB.config(text_color="black")

#fondo del las opciones de inicio de sesion
frame = CTkFrame(root, width=500, height=745, fg_color=negro)
frame.place(x=0, y=0)

#titulo del inicio de sesion
titulo = CTkLabel(root,text="Iniciar sesión", bg_color=negro, font=("Arial Rounded MT bold",50))
titulo.place(x=20,y=160)

#texto del logo
nombreLogo = CTkLabel(root,text="ROSSE", text_color=azul, bg_color=negro, font=("Audiowide",15))
nombreLogo.place(x=20,y=30)

#correo
tituloCorreo = CTkLabel(root, text="Correo", font=("Helvetica bold",20), bg_color=negro)
tituloCorreo.place(x=20, y=270)

correo_entry = CTkEntry(root, font=("sans serif", 12), placeholder_text="Correo electronico", 
                        border_color="grey", fg_color=negro, width=450, height=60)
correo_entry.place(x=20, y=300)

#contraseña
tituloContraseña = CTkLabel(root, text="contraseña", font=("Helvetica bold",20), bg_color=negro)
tituloContraseña.place(x=20, y=370)

contraseña_entry = CTkEntry(root, font=("sans serif", 12), placeholder_text="Contraseña ", 
                            border_color="grey", fg_color=negro, width=450, height=60)
contraseña_entry.place(x=20, y=400)

#boton de inicio de sesion
iniciarSesionB = CTkButton(root, text="Iniciar sesion", fg_color=azul, border_color=azul, text_color=negro,
                           width=450, height=60, cursor="hand2", command=iniciar_sesion)
iniciarSesionB.place(x=20, y=490)

#boton registrase
registrarseB = CTkLabel(root, text="¿No tienes cuenta? registrate aquí", font=("Helvetica bold",20),
                        bg_color=negro, cursor="hand2")
registrarseB.place(x=20, y=650)

registrarseB.bind("<Enter>", on_enter)
registrarseB.bind("<Leave>", on_leave)

root.mainloop()
