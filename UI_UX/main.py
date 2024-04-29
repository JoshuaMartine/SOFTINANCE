
import customtkinter
from PIL import Image, ImageTk
import sys
import requests
import json
import threading
import time
import replicate
import os
import google.generativeai as genai
import key

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self, user_email):
        super().__init__()

        # configure window
        self.title("ROSSE AI")
        self.geometry(f"{1100}x{580}")
        self.iconbitmap("./imagenes/a.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # create new chat icon
        image_path = "./imagenes/a.png"
        image = Image.open(image_path)
        image = image.resize((25, 20))
        photo = ImageTk.PhotoImage(image)
        new_chat_icon = customtkinter.CTkLabel(self.sidebar_frame, image=photo, text=" Nuevo Chat", compound='left')
        new_chat_icon.grid(row=0, column=0, padx=20, pady=(10, 10))

        # create another icon
        image_path = "./imagenes/newchat.png"
        image = Image.open(image_path)
        image = image.resize((15, 15))
        photo = ImageTk.PhotoImage(image)
        another_icon = customtkinter.CTkLabel(self.sidebar_frame, image=photo, text="")
        another_icon.grid(row=0, column=3, padx=20, pady=(10, 10))

        

        # create user icon

        
        image_path = "./imagenes/user.png"
        image = Image.open(image_path)
        image = image.resize((20, 20))
        photo = ImageTk.PhotoImage(image)
        user_email_label = customtkinter.CTkLabel(self.sidebar_frame, text="    " + user_email, compound='left')
        user_email_label.grid(row=5, column=0, padx=20, pady=(10, 10))
       

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Habla con ROSSE")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # create a btn enviar
        image_path = "./imagenes/enviar.png"
        image = Image.open(image_path)
        image = image.resize((20, 20))
        photo = ImageTk.PhotoImage(image)
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="#00c4cc", corner_radius=20, height=40, width=6,  hover_color=("gray75", "gray20"), text="", image=photo)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_1.configure(command=self.enviar_a_api)


        # crear botón de micrófono pequeño y redondo
        image_path = "./imagenes/microphone.png"
        image = Image.open(image_path)
        image = image.resize((20, 20))
        photo = ImageTk.PhotoImage(image)
        self.microphone_button = customtkinter.CTkButton(self, fg_color="#00c4cc", corner_radius=20, height=40, width=4,text="",  hover_color=("gray75", "gray20"), image=photo)
        self.microphone_button.image = image
        self.microphone_button.grid(row=3, column=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=1000, height=650)
        self.textbox.grid(row=0, column=1, columnspan=4, padx=(40, 40), pady=(40, 10), sticky="nsew")
       
        # establecer textbox en solo lectura
        self.textbox.configure(state="disabled")

        # create image and text to insert into textbox
        image_path = "./imagenes/a.png"
        image = Image.open(image_path)
        image = image.resize((350, 300))
        photo = ImageTk.PhotoImage(image)
        text = "¿Cómo puedo ayudarte hoy?"

        # create a label to display the image and text
        self.label = customtkinter.CTkLabel(self, text=text, image=photo, compound="top")
        self.label.grid(row=0, column=1, columnspan=4, padx=(40, 40), pady=(40, 10), sticky="nsew")

        # configure the font and weightof the text
        self.label.configure(font=("Arial black", 24))

        # schedule the deletion of the label after 3 seconds
        self.after(10000, self.delete_label)

    def delete_label(self):
        # delete the label
        self.label.destroy()


    def enviar_a_api(self):
     # Tomar el texto de entrada
        input_text = self.entry.get()
        self.textbox.configure(state='normal')
        self.textbox.insert('end', f"\nTú: {input_text}\n\n")
        self.entry.delete(0, 'end')  # Limpiar la entrada después de enviar

        # Deshabilitar la entrada y el botón mientras se obtiene la respuesta
        self.entry.configure(state='disabled')
        self.main_button_1.configure(state='disabled')

        # Iniciar un nuevo hilo para la solicitud de la API
        threading.Thread(target=self.obtener_respuesta_api, args=(input_text,)).start()
        threading.Thread(target=self.obtener_respuesta_api, args=(input_text,)).start()
 
    def obtener_respuesta_api(self, input_text):
        genai.configure(api_key=key.clave)
        model = genai.GenerativeModel(model_name="gemini-pro")

        # Realizar la consulta y obtener la respuesta
        consulta = input_text
        response = model.generate_content(consulta)

        # Actualizar el cuadro de texto con la respuesta de la API
        self.textbox.insert('end', f"\nROSSE AI: {response.text}\n")

        # Restablecer el estado de la entrada y el botón
        self.textbox.configure(state='disabled')
        self.entry.configure(state='normal')
        self.main_button_1.configure(state='normal')
        self.textbox.see('end') 
    # Cargar la API key desde una variable de entorno
    

if __name__ == "__main__":
    # Recupera el correo electrónico del argumento si existe, de lo contrario usa un valor predeterminado
    email_arg = sys.argv[1] if len(sys.argv) > 1 else "username@fulanito"
    app = App(email_arg)
    app.mainloop()


