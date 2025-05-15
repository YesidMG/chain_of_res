from validators.base_validator import Validator

class NombreValidator(Validator):
    def validate(self, nombre):
        if not nombre.strip():
            print("Error: El nombre no puede estar vacío.")
            return False
        return self.next(nombre)
