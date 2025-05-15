from validators.base_validator import Validator

class NombreValidator(Validator):
    def validate(self, nombre, errors):
        if not nombre.strip():
            errors.append("Error: El nombre no puede estar vacío.")
        return self.next(nombre, errors)
