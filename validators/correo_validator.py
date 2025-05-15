from validators.base_validator import Validator
import re

class CorreoValidator(Validator):
    def validate(self, correo):
        if correo.count('@') != 1:
            print("Error: El correo debe contener un único '@'.")
            return False
        # Validación simple de formato (puedes mejorar)
        patron = r'^[^@]+@[^@]+\.[^@]+$'
        if not re.match(patron, correo):
            print("Error: Formato de correo inválido.")
            return False
        return self.next(correo)
