from validators.base_validator import Validator

class CorreoValidator(Validator):
    def validate(self, correo, errors):
        # Asegúrate de que el correo sea una cadena
        if not isinstance(correo, str):
            errors.append("Error: El correo debe ser una cadena de texto.")
            return self.next(correo, errors)

        # Validar que contenga exactamente un '@'
        if correo.count('@') != 1:
            errors.append("Error: El correo debe contener un único '@'.")
        return self.next(correo, errors)
