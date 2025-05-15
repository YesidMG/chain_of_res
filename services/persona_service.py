from models.persona import Persona

class PersonaService:
    def __init__(self):
        self.personas = []

    def registrar_persona(self, cc, nombre, telefono, correo, direccion):
        persona = Persona(cc, nombre, telefono, correo, direccion)
        self.personas.append(persona)

    def existe_cc(self, cc):
        return any(p.cc == cc for p in self.personas)

    def buscar_por_cc(self, cc):
        for p in self.personas:
            if p.cc == cc:
                return p
        return None

    def listar_personas(self):
        if not self.personas:
            print("No hay personas registradas.")
            return
        print("\n--- Lista de Personas ---")
        for p in self.personas:
            print(f"- CC:{p.cc} / {p.nombre}")
