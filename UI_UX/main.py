import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
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
        new_chat_icon = customtkinter.CTkLabel(self.sidebar_frame, image=photo, text="")
        new_chat_icon.grid(row=0, column=0, padx=20, pady=(10, 10))

        # create another icon
        image_path = "./imagenes/newchat.png"
        image = Image.open(image_path)
        image = image.resize((15, 15))
        photo = ImageTk.PhotoImage(image)
        another_icon = customtkinter.CTkLabel(self.sidebar_frame, image=photo, text="")
        another_icon.grid(row=0, column=3, padx=20, pady=(10, 10))

        # logo label
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="new chat", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=20, pady=(10, 10))

        # create auser icon
        image_path = "./imagenes/user.png"
        image = Image.open(image_path)
        image = image.resize((20, 20))
        photo = ImageTk.PhotoImage(image)
        another_icon = customtkinter.CTkLabel(self.sidebar_frame, image=photo, text="")
        another_icon.grid(row=5, column=0, padx=20, pady=(10, 10))
        self.username = customtkinter.CTkLabel(self.sidebar_frame, text="username@fulanito", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.username.grid(row=5, column=1, padx=20, pady=(10, 10))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Habla con ROSSE")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # create a btn enviar
        image_path = "./imagenes/enviar.png"
        image = Image.open(image_path)
        image = image.rotate(90)
        image = image.resize((20, 20))
        photo = ImageTk.PhotoImage(image)
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="#00c4cc", corner_radius=20, height=40, width=40,  hover_color=("gray75", "gray20"), text="", image=photo)
        self.main_button_1.image = image
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # crear botón de micrófono pequeño y redondo
        image_path = "./imagenes/microphone.png"
        image = Image.open(image_path)
        image = image.resize((20, 20))
        photo = ImageTk.PhotoImage(image)
        self.microphone_button = customtkinter.CTkButton(self, fg_color="#00c4cc", corner_radius=20, height=30, width=30,text="", image=photo)
        self.microphone_button.image = image
        self.microphone_button.grid(row=3, column=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=1000, height=650)
        self.textbox.grid(row=0, column=1, columnspan=4, padx=(40, 40), pady=(40, 10), sticky="nsew")

        # set default values
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 2)

if __name__ == "__main__":
    app = App()
    app.mainloop()