class Persona:
    def __init__(self, cc, nombre, telefono, correo, direccion):
        self.cc = cc
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        return (
            f"Cédula: {self.cc}\n"
            f"Nombre: {self.nombre}\n"
            f"Teléfono: {self.telefono}\n"
            f"Correo: {self.correo}\n"
            f"Dirección: {self.direccion}"
        )
