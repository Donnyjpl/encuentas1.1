from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False, alternativas=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.__alternativas = [Alternativa(**alt) for alt in alternativas] if alternativas else []

    def mostrar_pregunta(self):
        print("Enunciado:", self.enunciado)
        if self.ayuda:
            print("Ayuda:", self.ayuda)  # Accede al atributo ayuda si está presente
        print("Requerida:", self.requerida)
        for alternativa in self.__alternativas:
            alternativa.mostrar_alternativa()

    def get_enunciado(self):
        return self.enunciado
    def get_ayuda(self):
        return self.ayuda
# Ejemplo de uso
alternativas = [
    {"contenido": "Opción A", "ayuda": "Ayuda para la opción A"},
    {"contenido": "Opción B", "ayuda": "Ayuda para la opción B"}
]

pregunta = Pregunta("¿Cuál es tu opción favorita?", "Selecciona tu opción favorita", True, alternativas)
pregunta.mostrar_pregunta()
