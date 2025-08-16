# main.py
# Importar 
from gestor_datos import GestorExperimentos
from notificacion import leer_en_voz, enviar_whatsapp
from planificador import iniciar_planificador
from datetime import datetime

def mostrar_menu(): # Muestra las acciones disponibles como un menú
    print("Asistente de laboratorio Químico")
    print("1. Registrar un nuevo experimento")
    print("2. Hacer un gráfico de barras con el rendimiento")
    print("3. Enviar recordatorio manual por WhatsApp")
    print("4. Agregar nueva tarea")
    print("5. Ver tareas pendientes") 
    print("6. Salir")
    return input("¿Qué quieres hacer? Elige un número (1-6): ")

# Función principal
def main():
    # Objeto para manejar los experimentos y tareas
    gestor = GestorExperimentos()

    leer_en_voz("Asistente de química iniciado.")

    # Se ejecuta el planificador de tareas
    iniciar_planificador()

    # Inicio del programa hasta elegir salir
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            # Dar datos del experimento
            nombre = input("Nombre del experimento: ")
            reactivos = input("Reactivos que usaste (ej: HCl, NaCl): ")
            resultado = input("¿Qué se obtuvo?): ") # Calculos. constantes, objetivos
            rendimiento = float(input("Rendimiento porcentual (pon un número): "))
            fecha = datetime.now().strftime("%Y-%m-%d") # La fecha de hoy

            # Se guarda
            gestor.agregar_experimento(nombre, fecha, reactivos, resultado, rendimiento)
            leer_en_voz("Registrado")

        elif opcion == '2':
            print("Creando el gráfico de barras...")
            gestor.generar_grafico_rendimiento() # Creación de el gráfico de rendimiento
            leer_en_voz("Gráfico creado. Búscalo en la carpeta 'graficos'.")

        elif opcion == '3':
            numero = input("Ingresa tu número de teléfono (formato +códigoPaísNumero, ej: +525588356814): ")
            mensaje = input("¿Qué mensaje quieres enviar?: ") 
            enviar_whatsapp(numero, mensaje) #Se envia por WhatsApp Web
        
        elif opcion == '4':
            descripcion = input("Describe la tarea: ") # Descripción de la tarea
            fecha_limite = input("¿Para cuándo es? (formato AAAA-MM-DD): ")
            gestor.agregar_tarea(descripcion, fecha_limite) # Agrega la tarea al gestor
            leer_en_voz("Tarea guardada.")


        elif opcion == '5':
            gestor.mostrar_tareas() # Muestra las tareas pendientes

        elif opcion == '6':
            leer_en_voz("¡Hasta luego!")
            break # Cierre

        else:
            print("Esa opción no existe, por favor elige un número del 1 al 6.")

print("Gracias por usar el asistente del laboratorio Químico!")
if __name__ == "__main__":
    main() 