from usuario import Usuario
from encuesta import Encuesta
from encuestaler import EncuestaLE, EncuestaLR
from listado_respuestas import ListadoRespuestas
from preguntas import Pregunta

# Crear instancias de usuario, preguntas, encuestas, etc.
usuario = Usuario("ejemplo@example.com", 30, "Norte")

# Crear encuesta por región
preguntas_region = [
    Pregunta("¿Te gusta la comida picante?", ayuda="Responde sí o no"),
    Pregunta("¿Cuál es tu plato regional favorito?", ayuda="Escribe el nombre de tu plato favorito")
]
encuesta_region = EncuestaLR("Encuesta Gastronómica", ["Norte", "Centro", "Sur"], preguntas_region)

# Asignar encuesta por región al usuario
usuario.asignar_encuesta_por_region(encuesta_region)

# Crear encuesta por edad
preguntas_edad = [
    Pregunta("¿Estás satisfecho con tu vida actual?", ayuda="Responde sí o no"),
    Pregunta("¿Cuál es tu mayor aspiración en la vida?", ayuda="Describe tu mayor aspiración en una oración")
]
encuesta_edad = EncuestaLE("Encuesta de Satisfacción", 25, 40, preguntas_edad)

# Asignar encuesta por edad al usuario
usuario.asignar_encuesta_por_edad(25, 40, encuesta_edad)

# Responder encuestas
usuario.responder_encuesta(encuesta_edad)
usuario.responder_encuesta(encuesta_region)

# Mostrar las respuestas del usuario
for listado_respuestas in usuario.listados_respuestas:
    print(listado_respuestas.lista_respuesta)
