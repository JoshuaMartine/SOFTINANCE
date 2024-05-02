import customtkinter
from PIL import Image, ImageTk
import sys
import threading
import google.generativeai as genai
import key
import tkinter as tk
from tkinter import Listbox
import os

# Configuración de la apariencia y el tema
customtkinter.set_appearance_mode("Dark")  # Modos: "System" (estándar), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Temas: "blue" (estándar), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self, user_email):
        super().__init__()

        self.title("ROSSE AI")
        self.geometry(f"{1100}x{580}")
        self.iconbitmap("./imagenes/a.ico")
        self.configure_grid()
        self.create_sidebar(user_email)
        self.create_main_area()
        self.create_conversation_history_frame()
        self.create_footer()
        self.load_api_key()

    def configure_grid(self):
        # Configura el diseño de la cuadrícula (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def create_sidebar(self, user_email):
        # Crea la barra lateral con widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0, fg_color="#212121")
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Icono de nuevo chat
        self.create_icon("./imagenes/a.png", " Nuevo Chat", self.sidebar_frame, 25, 20, 0)

        # Icono de usuario
        self.create_icon("./imagenes/user.png", "    " + user_email, self.sidebar_frame, 20, 20, 5)

    def create_icon(self, path, text, frame, width, height, row):
        image = Image.open(path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        label = customtkinter.CTkLabel(frame, image=photo, text=text, compound='left')
        label.image = photo  # keep a reference!
        label.grid(row=row, column=0, padx=20, pady=(10, 10))

    def create_main_area(self):
        # Crea la zona principal
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Habla con ROSSE")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self, width=1000, height=650, state="disabled", fg_color="#212121", font=("Helvetica bold",12))
        self.textbox.grid(row=0, column=1, columnspan=4, padx=(40, 40), pady=(40, 10), sticky="nsew")

    def create_conversation_history_frame(self):
    # Configura el frame para el historial de conversaciones
        self.conversation_history_frame = customtkinter.CTkFrame(self.sidebar_frame, corner_radius=0)
        self.conversation_history_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))
        self.conversation_history_frame.grid_rowconfigure(0, weight=1)
        self.conversation_history_frame.grid_columnconfigure(0, weight=1)
        
        bg_color = self.sidebar_frame.cget("bg")
        fg_color = ""

        # Crea una lista para mostrar el historial
        self.conversation_listbox = customtkinter.CTkListbox(self.conversation_history_frame)
        self.conversation_listbox.grid(row=0, column=0, sticky="nsew", padx=10)

    def create_footer(self):
        # Crea el footer con botones de enviar y micrófono
        self.create_send_button()
        self.create_microphone_button()

    def create_send_button(self):
        self.send_button = self.create_button("./imagenes/enviar.png", "", self.send_to_api, 20, 20)
        self.send_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
    
    

    #AQUI ES DONDE ESTA LA CONEXION DEL BOTON
    def create_microphone_button(self):
     self.microphone_button = self.create_button("./imagenes/microphone.png", "", self.run_test_py, 20, 20)
     self.microphone_button.grid(row=3, column=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

    def run_test_py(self):
     import subprocess
     import sys
    
     # Construir la ruta absoluta al archivo
     script_path = os.path.join(os.path.dirname(__file__), 'test.py')
    
     # Verificar si el archivo existe antes de intentar ejecutarlo
     if os.path.exists(script_path):
        # Llamar al script de Python de manera segura
        subprocess.run([sys.executable, script_path])
     else:
        print(f"Error: No se encontró el archivo {script_path}")
    #AQUI TERMINA LA CONEXION DEL BOTON

    def create_button(self, path, text, command, width, height):
        image = Image.open(path)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        button = customtkinter.CTkButton(self, image=photo, text=text, command=command, fg_color="#00c4cc", corner_radius=20, height=40, width=6, hover_color=("gray75", "gray20"))
        button.image = photo  # keep a reference!
        return button

    def send_to_api(self):
        # Toma el texto de entrada y lo envía a la API
        input_text = self.entry.get()
        self.textbox.configure(state='normal')
        self.textbox.insert('end', f"\nTú: {input_text}\n\n")
        self.update_conversation_history(f"Tú: {input_text}")
        self.entry.delete(0, 'end')  # Limpia la entrada después de enviar
        self.entry.configure(state='disabled')
        self.send_button.configure(state='disabled')
        threading.Thread(target=self.get_response_from_api, args=(input_text,)).start()

    def get_response_from_api(self, input_text):
     try:
        genai.configure(api_key=key.clave)
        model = genai.GenerativeModel(model_name="gemini-pro")
        
        print(f"Enviando a la API: {input_text}")  # Debug print, remove in production
        response = model.generate_content(input_text)

        if response.text:
            print(f"Respuesta de la API: {response.text}")  # Debug print, remove in production
            self.textbox.configure(state='normal')
            self.textbox.insert('end', f"\nROSSE AI: {response.text}\n")
            self.textbox.configure(state='disabled')
        else:
            print("No hubo respuesta de la API.")  # Debug print, remove in production
     except Exception as e:
        print(f"Se produjo un error al obtener la respuesta de la API: {e}")  # Debug print, remove in production
     finally:
        # Restablecer el estado de la entrada y el botón independientemente del resultado
        self.entry.configure(state='normal')
        self.send_button.configure(state='normal')
        self.textbox.see('end') 

# Recuerda remover los print statements antes de lanzar la aplicación.


    def update_conversation_history(self, message):
        # Inserta el nuevo mensaje al principio de la lista
        self.conversation_listbox.insert(0, message)
        # Limita la cantidad de mensajes mostrados
        if self.conversation_listbox.size() > 100:
            self.conversation_listbox.delete(100)

    def load_api_key(self):
        # Carga la API key desde una variable de entorno
        # Esta función debe implementarse con tu lógica de carga de clave API
        pass
    
    
    def create_conversation_history_frame(self):
        # Configura el frame para el historial de conversaciones
        self.conversation_history_frame = customtkinter.CTkFrame(self.sidebar_frame, corner_radius=0)
        self.conversation_history_frame.grid(row=1, column=0, sticky="nsew", pady=(20, 0))
        self.conversation_history_frame.grid_rowconfigure(0, weight=1)
        self.conversation_history_frame.grid_columnconfigure(0, weight=1)

        # Crea un Listbox estándar de Tkinter para mostrar el historial
        self.conversation_listbox = Listbox(self.conversation_history_frame, bg="#212121", fg="white", borderwidth=0, highlightthickness=0)
        self.conversation_listbox.grid(row=0, column=0, sticky="nsew", padx=10)

if __name__ == "__main__":
    email_arg = sys.argv[1] if len(sys.argv) > 1 else "username@fulanito"
    app = App(email_arg)
    app.mainloop()