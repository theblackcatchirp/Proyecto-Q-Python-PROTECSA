# gestor_datos.py
import pandas as pd
import os
import matplotlib.pyplot as plt

class GestorExperimentos:
    def __init__(self, archivo_experimentos='datos/experimentos.csv', archivo_tareas='datos/tareas.csv'):
        self.experimentos_path = archivo_experimentos
        self.tareas_path = archivo_tareas
        # Para verificar que las carpetas existen y sino crearlas
        os.makedirs('datos', exist_ok=True)
        os.makedirs('graficos', exist_ok=True)
        self.df = self.cargar_datos_exp()
        self.df_tareas = self.cargar_datos_tareas()

    def cargar_datos_exp(self):
        try:
            # Lectura del el archivo CSV
            df = pd.read_csv(self.experimentos_path)
            return df
        except FileNotFoundError:
            # Cuando no exista el documento, se crea uno vacío con las columnas
            print("Archivo CSV no encontrado. Se creará uno nuevo.")
            return pd.DataFrame(columns=['ID', 'Nombre', 'Fecha', 'Reactivos', 'Resultado', 'Rendimiento'])
        
    def cargar_datos_tareas(self):
        try:
            df = pd.read_csv(self.tareas_path) # Lectura del archivo CSV de tareas
            return df
        except FileNotFoundError:
            print("Archivo de tareas no encontrado. Creando uno nuevo.")
            return pd.DataFrame(columns=['ID', 'Descripcion', 'Fecha_Limite', 'Estado'])

    def guardar_datos_exp(self): # Guarda los datos de experimentos
        self.df_experimentos.to_csv(self.experimentos_path, index=False)
        print("Datos de experimentos guardados")
    
    def guardar_datos_tareas(self): # Guarda los datos de tareas
        self.df_tareas.to_csv(self.tareas_path, index=False)
        print("¡Datos de tareas guardados!")


    def agregar_experimento(self, nombre, fecha, reactivos, resultado, rendimiento):
        """Agrega un nuevo experimento."""
        # Determina el nuevo ID sumando 1 al ID más alto existente
        nuevo_id = self.df['ID'].max() + 1 if not self.df.empty else 1

        nuevo_experimento = {
            'ID': nuevo_id,
            'Nombre': nombre,
            'Fecha': fecha,
            'Reactivos': reactivos,
            'Resultado': resultado,
            'Rendimiento': rendimiento
        }

        # Agrega la nueva fila
        self.df = pd.concat([self.df, pd.DataFrame([nuevo_experimento])], ignore_index=True)
        self.guardar_datos()
        print(f"Experimento '{nombre}' agregado con éxito.")
    
     # Función para agregar tareas
    def agregar_tarea(self, descripcion, fecha_limite):
        nuevo_id = self.df_tareas['ID'].max() + 1 if not self.df_tareas.empty else 1
        nueva_tarea = {
            'ID': nuevo_id,
            'Descripcion': descripcion,
            'Fecha_Limite': fecha_limite,
            'Estado': 'Pendiente' # Todas las tareas nuevas empiezan como pendientes
        }
        self.df_tareas = pd.concat([self.df_tareas, pd.DataFrame([nueva_tarea])], ignore_index=True)
        self.guardar_datos_tareas()
        print(f"Tarea '{descripcion}' agregada.")

    # ver la lista de tareas que hay
    def mostrar_tareas(self):
        if self.df_tareas.empty:
            print("No hay tareas pendientes.")
        else:
            print("LISTA DE TAREAS")
            
            print(self.df_tareas.to_string(index=False))
            print("------------------------")

    def generar_grafico_rendimiento(self):
        """Genera y guarda un gráfico de barras"""
        if self.df.empty or len(self.df) < 1:
            print("No hay suficientes datos para crear un gráfico.")
            return

        # Toma los últimos 7 experimentos
        datos_recientes = self.df.tail(7)

        plt.figure(figsize=(10, 6)) # Crea un lienzo para el gráfico
        plt.bar(datos_recientes['Nombre'], datos_recientes['Rendimiento'], color='skyblue')

        # Para agregar etiquetas y título
        plt.title('Experimentos 2025')
        plt.xlabel('Nombre del experimento')
        plt.ylabel('Rendimiento (%)')
        plt.xticks(rotation=15, ha='right') # Rota las etiquetas
        plt.tight_layout() # Ajuste de grafico

        # Guardamos el gráfico como una imagen PNG
        ruta_guardado = 'graficos/rendimiento_experimentos.png'
        plt.savefig(ruta_guardado)
        plt.close() # Cierre

        print(f"Gráfico guardado en: {ruta_guardado}")