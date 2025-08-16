# notificador.py
import pyttsx3 # Para la voz
import pywhatkit # Para mandar mensajes por WhatsApp

def leer_en_voz(texto):
    try:
        engine = pyttsx3.init() # Inicializa el motor de voz
        engine.say(texto)
        engine.runAndWait() # Ejecuta la voz
    except Exception as e:
        print(f"Hubo un problema con el motor de voz: {e}")

def enviar_whatsapp(numero_destino, mensaje):
    try:
        pywhatkit.sendwhatmsg_instantly(numero_destino, mensaje, wait_time=15) # Envía el mensaje de WhatsApp
        print("Abriendo WhatsApp para mandar el mensaje...") 
    except Exception as e:
        print(f"No se mando el mensaje: {e}")