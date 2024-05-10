from encuesta import Encuesta
from listado_respuestas import ListadoRespuestas  # Importar la clase ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        self.__correo = correo
        self.__edad = edad
        self.__region = region
        self.__encuesta_actual = None 
        self.__listados_respuestas = []
        self.__encuesta_por_edad = {}
        self.__encuesta_por_region = {}
        
    @property
    def correo(self):
        return self.__correo
    
    @property
    def listados_respuestas(self):
        return self.__listados_respuestas
    
    def agregar_listado_respuestas(self, listado_respuestas):
        self.__listados_respuestas.append(listado_respuestas)
    
    def asignar_encuesta_por_edad(self, edad_minima, edad_maxima, encuesta):
        self.__encuesta_por_edad[(edad_minima, edad_maxima)] = encuesta
    
    # En la clase Usuario
    def asignar_encuesta_por_region(self, encuesta):
        region = encuesta.obtener_region(1)    # Selecciona la primera región por defecto
        self.__encuesta_por_region[region] = encuesta
    def responder_encuesta(self, encuesta):
        print(f"¡Bienvenido, {self.correo}! Vamos a responder la encuesta '{encuesta.nombre}'.")
        respuestas = {}
        for pregunta in encuesta.preguntas:
            print(f"\n{pregunta.get_enunciado()}")
            if pregunta.get_ayuda():
                print(f"Ayuda: {pregunta.get_ayuda()}")

            respuesta_usuario = input("Ingresa tu respuesta: ")
            respuestas[pregunta.get_enunciado()] = respuesta_usuario

        # Corregir el nombre de la clase y crear la instancia
        listado_respuestas = ListadoRespuestas(self, respuestas)
        self.agregar_listado_respuestas(listado_respuestas)

        print("\n¡Encuesta respondida con éxito!")


   
    @property
    def encuesta_actual(self):
        return self.__encuesta_actual
    
    @encuesta_actual.setter
    def encuesta_actual(self, encuesta):
        self.__encuesta_actual = encuesta
