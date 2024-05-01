import speech_recognition as sr
import google.generativeai as genai
import key2
import threading

# Inicializa el reconocedor de voz
r = sr.Recognizer()

def get_response_from_api(input_text):
    try:
        genai.configure(api_key=key2.clave2)
        model = genai.GenerativeModel(model_name="gemini-pro")
        
        print(f"Enviando a la API: {input_text}")  # Debug print, remove in production
        response = model.generate_content(input_text)

        if response.text:
            print(f"Respuesta de la API: {response.text}")  # Debug print, remove in production
        else:
            print("No hubo respuesta de la API.")  # Debug print, remove in production
    except Exception as e:
        print(f"Se produjo un error al obtener la respuesta de la API: {e}")  # Debug print, remove in production

def send_to_api(solicitud):
    threading.Thread(target=get_response_from_api, args=(solicitud,)).start()

# Usa el micrófono como fuente de audio
with sr.Microphone() as source:
    print("Habla ahora, te estoy escuchando...")
    audio = r.listen(source)

    try:
        # Usa el reconocedor de Google para audio
        text = r.recognize_google(audio, language='es-ES')
        print(text)
        send_to_api(text)  # Envía el texto a la API
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio")
    except sr.RequestError as e:
        print(f"No se pudo solicitar resultados desde el servicio de Google Speech Recognition; {e}")

# Espera que todos los threads se completen
for thread in threading.enumerate():
    if thread is not threading.currentThread():
        thread.join()
