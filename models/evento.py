from datetime import datetime

class Evento:
    _id_counter = 1

    def __init__(self, nombre, direccion, fecha, duenio, descripcion):
        self.id = Evento._id_counter
        Evento._id_counter += 1

        self.nombre = nombre
        self.direccion = direccion
        self.fecha = fecha  
        self.duenio = duenio 
        self.descripcion = descripcion
        self.personal = [] 

    def agregar_personal(self, personal_evento):
        self.personal.append(personal_evento)

    def __str__(self):
        personal_str = "\n".join([f"{p.persona.nombre} - {p.rol}" for p in self.personal]) or "No hay personal asignado"
        return (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Dirección: {self.direccion}\n"
            f"Fecha: {self.fecha.strftime('%Y-%m-%d')}\n"
            f"Dueño: {self.duenio.nombre}\n"
            f"Descripción: {self.descripcion}\n"
            f"Personal:\n{personal_str}"
        )
