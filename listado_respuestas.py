class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        self.usuario = usuario
        self.respuestas = respuestas
    @property
    def lista_respuesta(self):
        return f"Listado de Respuestas de {self.usuario}: {self.respuestas}"