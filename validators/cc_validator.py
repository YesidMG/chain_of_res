from validators.base_validator import Validator

class CCValidator(Validator):
    def __init__(self, existing_ccs):
        super().__init__()
        self.existing_ccs = existing_ccs

    def validate(self, cc, errors):
        if not cc.isdigit():
            errors.append("Error: La cédula debe contener solo números positivos.")
        if cc in self.existing_ccs:
            errors.append("Error: La cédula ya está registrada.")
        return self.next(cc, errors)
