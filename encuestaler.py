from encuesta import Encuesta

class EncuestaLE(Encuesta):
    def __init__(self, nombre, edad_minima, edad_maxima, preguntas=None, listados_respuestas=None):
        super().__init__(nombre, preguntas, listados_respuestas)
        self.__edad_minima = edad_minima
        self.__edad_maxima = edad_maxima
class EncuestaLR(Encuesta):
    def __init__(self, nombre, regiones, preguntas=None, listados_respuestas=None):
        super().__init__(nombre, preguntas, listados_respuestas)
        self.__regiones = regiones
        
    def obtener_region(self, numero):
        if 1 <= numero <= len(self.__regiones):
            return self.__regiones[numero - 1]
        else:
            return None


