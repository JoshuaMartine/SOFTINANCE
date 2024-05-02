import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
import key2
import threading

# Inicializa el reconocedor de voz y el motor de TTS (text-to-speech)
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    # Obtiene y selecciona la voz en español
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'spanish' in voice.name.lower():  # Cambia 'spanish' por el identificador adecuado si es necesario
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
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
            print("No hubo respuesta de la API.")
            speak("No hubo respuesta de la API.")
    except Exception as e:
        print(f"Se produjo un error al obtener la respuesta de la API: {e}")
        speak(f"Se produjo un error al obtener la respuesta de la API: {e}")

def send_to_api(solicitud):
    threading.Thread(target=get_response_from_api, args=(solicitud,)).start()

# Usa el micrófono como fuente de audio
with sr.Microphone() as source:
    print("Habla ahora, te estoy escuchando...")
    speak("Habla ahora, te estoy escuchando.")
    audio = r.listen(source)

    try:
        # Usa el reconocedor de Google para audio
        text = r.recognize_google(audio, language='es-ES')
        print(text)
        speak(f"Recibido: {text}")
        send_to_api(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition no pudo entender el audio")
        speak("No pude entender el audio")
    except sr.RequestError as e:
        print(f"No se pudo solicitar resultados desde el servicio de Google Speech Recognition; {e}")
        speak(f"Error de servicio: {e}")

# Espera que todos los threads se completen
for thread in threading.enumerate():
    if thread is not threading.currentThread():
        thread.join()
