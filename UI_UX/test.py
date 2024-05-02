import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
import key2
import threading

# Inicializa el reconocedor de voz y el motor de TTS (text-to-speech)
r = sr.Recognizer()
engine = pyttsx3.init()

def clean_text(text):
    # Define aquí los caracteres que deseas eliminar o reemplazar
    text = text.replace('*', '')  # Elimina asteriscos
    text = text.replace('#', '')  # Elimina almohadillas, añade más líneas como esta si es necesario
    return text

def speak(text):
    cleaned_text = clean_text(text)  # Limpia el texto antes de hablarlo
    # Obtiene y selecciona la voz en español
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'spanish' in voice.name.lower():  # Cambia 'spanish' por el identificador adecuado si es necesario
            engine.setProperty('voice', voice.id)
            break
    engine.say(cleaned_text)
    engine.runAndWait()

def get_response_from_api(input_text):
    try:
        genai.configure(api_key=key2.clave2)
        model = genai.GenerativeModel(model_name="gemini-pro")
        
        print(f"Enviando a la API: {input_text}")
        response = model.generate_content(input_text)

        if response.text:
            print(f"Respuesta de la API: {response.text}")
            speak(response.text)
        else:
            print("Rosse no pudo procesar una respuesta.")
            speak("Rrous no pudo procesar una respuesta.")
    except Exception as e:
        print(f"Se produjo un error al obtener la respuesta de la API: {e}")
        speak(f"Se produjo un error al obtener la respuesta de la API: {e}")

def send_to_api(solicitud):
    threading.Thread(target=get_response_from_api, args=(solicitud,)).start()

def listen_and_respond():
    print("Hola, soy Rosse, ¿en que puedo ayudarte el día de hoy?")
    speak("Hola, soy Rrous, ¿en que puedo ayudarte el día de hoy?")
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='es-ES')
                print(" ")
                send_to_api(text)
            except sr.UnknownValueError:
                print("No pude entender el audio")
                speak("No pude entender el audio, intenta de nuevo.")
            except sr.RequestError as e:
                print(f"Error de servicio: {e}")
                speak(f"Error de servicio: {e}")

# Inicia el ciclo de escucha y respuesta
listen_and_respond()
