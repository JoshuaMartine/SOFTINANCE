from customtkinter import *
import ctypes
from tkinter import *
from math import cos, sin, radians, pi

# Obtener el tamaño de la pantalla
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
azulFondo = "#031e35"
azulEnfoque = "#00c4cc"

#creación y configuración de la ventana
root = CTk()
root.title("ROSSE AI")
root.iconbitmap("./imagenes/a.ico")
set_appearance_mode("dark")
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.config(background=azulFondo)


imagen_actual = 0  

def cambiar_imagen(event):
    global imagen_actual
    
    if imagen_actual == 0:
        pause_label.configure(image=otra_imagen)
        imagen_actual = 1
    else:
        pause_label.configure(image=pause)
        imagen_actual = 0

def talk(event):
    print("se presionó el microfono")

def cex(event):
    print("se presionó cancel")
    
def cambiar_imagen_enter(event):
    cancel_label.configure(image=otra_imagen1)

def cambiar_imagen_leave(event):
    cancel_label.configure(image=cancel)


#imagenes
imagen = PhotoImage(file="./imagenes/a.png")
imagen = imagen.subsample(15,15)
imagen_label = CTkLabel(root, image=imagen, text="", bg_color=azulFondo)
imagen_label.place(x=20, y=20)

#imagenes
circulo = PhotoImage(file="./imagenes/circulo.png")
circulo = circulo.subsample(1,1)
circulo_label = CTkLabel(root, image=circulo, text="", bg_color=azulFondo, cursor="hand2")
circulo_label.place(x=425, y= 55)



cancel = PhotoImage(file="./imagenes/boton-eliminar.png")
cancel = cancel.subsample(5, 5)
otra_imagen1 = PhotoImage(file="./imagenes/boton-eliminar-hover.png")
otra_imagen1 = otra_imagen1.subsample(5, 5)
cancel_label = CTkLabel(root, image=cancel, text="", bg_color=azulFondo, cursor="hand2")
cancel_label.bind("<Enter>", cambiar_imagen_enter)
cancel_label.bind("<Leave>", cambiar_imagen_leave)
cancel_label.place(x=876, y=570)


microfono = PhotoImage(file="./imagenes/microfono.png")
microfono = microfono.subsample(2,2)
microfono_label = CTkLabel(root, image=microfono, text="", bg_color=azulFondo, cursor="hand2")
microfono_label.place(x=550, y=175)
microfono_label.bind("<Button-1>", talk)

pause = PhotoImage(file="./imagenes/pausa.png")
pause = pause.subsample(5, 5)

# Crea la segunda imagen y la submuestrea
otra_imagen = PhotoImage(file="./imagenes/boton-de-play.png")
otra_imagen = otra_imagen.subsample(5, 5)

# Crea el CTkLabel con la primera imagen
pause_label = CTkLabel(root, image=pause, text="", bg_color=azulFondo, cursor="hand2")
pause_label.place(x=380, y=570)

# Asocia la función cambiar_imagen con el evento de clic
pause_label.bind("<Button-1>", cambiar_imagen)










root.mainloop()
