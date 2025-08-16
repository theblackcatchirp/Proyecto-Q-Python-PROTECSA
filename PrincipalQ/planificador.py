# planificador.py
import schedule # El organizador de tareas
import time
import threading # Para ejecutar tareas en segundo plano
from notificacion import leer_en_voz

def tarea_diaria():
    mensaje = "¡Hola, es hora de tu tarea diaria. Revisa tus experimentos y tareas pendientes."
    print("Ejecutando la tarea diaria...")
    leer_en_voz(mensaje)

def correr_planificador():
    # Determinamos qué tarea hacer y cuándo
    schedule.every().day.at("09:00").do(tarea_diaria)

    while True:
        schedule.run_pending()
        time.sleep(1) # Descansa un segundo

def iniciar_planificador():
    # en segundo plano se inicia el planificador
    hilo = threading.Thread(target=correr_planificador, daemon=True)
    hilo.start()
    print("El planificador de tareas ya está siendo ejecutado en segundo plano.")