from abc import ABC, abstractmethod
from preguntas import Pregunta

class Encuesta(ABC):
    def __init__(self, nombre, preguntas=None, listados_respuestas=None):
        self.__nombre = nombre
        self.preguntas = preguntas if preguntas else []  # Agrega este atributo
        self.listados_respuestas = listados_respuestas if listados_respuestas else []
        
    @property
    def nombre(self):
        return self.__nombre    

    def mostrar_encuesta(self):
        print("Nombre de la encuesta:", self.__nombre)
        for pregunta in self.__preguntas:
            pregunta.mostrar_pregunta()

    def agregar_listado_respuestas(self, listado_respuestas):
        self.__listados_respuestas.append(listado_respuestas)

