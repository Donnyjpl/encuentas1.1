class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self._contenido = contenido
        self._ayuda = ayuda
    
    @property
    def contenido(self):
        return self._contenido
    
    @property
    def ayuda(self):
        return self._ayuda
     
    def mostrar_alternativa(self):
        print("Contenido:", self._contenido)
        if self._ayuda:
            print("Ayuda:", self._ayuda)
