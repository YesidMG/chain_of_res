from models.evento import Evento
from models.personal_evento import PersonalEvento

class EventoService:
    def __init__(self, persona_service):
        self.eventos = []
        self.persona_service = persona_service  # Para buscar personas
     
    def listar_eventos(self):
        if not self.eventos:
            print("No hay eventos registrados.")
            return
        for e in self.eventos:
            print(f"{e.id} - {e.nombre}")

    def buscar_evento_por_id(self, id_evento):
        for e in self.eventos:
            if e.id == id_evento:
                return e
        return None

    def registrar_evento(self, nombre, direccion, fecha, cc_duenio, descripcion):
        # Buscar persona dueña
        duenio = self.persona_service.buscar_por_cc(cc_duenio)
        if not duenio:
            print("No existe persona con esa cédula para dueño del evento.")
            return None

        evento = Evento(nombre, direccion, fecha, duenio, descripcion)

        # Para asignar personal, se debe hacer fuera, usando agregar_personal

        self.eventos.append(evento)
        print(f"Evento '{nombre}' registrado con ID {evento.id}")
        return evento

    def asignar_personal(self, evento, cc_persona, rol):
        persona = self.persona_service.buscar_por_cc(cc_persona)
        if not persona:
            print("No existe persona con esa cédula.")
            return False
        personal_evento = PersonalEvento(persona, rol)
        evento.agregar_personal(personal_evento)
        print(f"Personal '{persona.nombre}' asignado con rol '{rol}' al evento '{evento.nombre}'.")
        return True
