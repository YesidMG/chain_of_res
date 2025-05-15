from validators.base_validator import Validator

class CCValidator(Validator):
    def __init__(self, existing_ccs):
        super().__init__()
        self.existing_ccs = existing_ccs

    def validate(self, cc):
        if not cc.isdigit():
            print("Error: La cédula debe contener solo números positivos.")
            return False
        if cc in self.existing_ccs:
            print("Error: La cédula ya está registrada.")
            return False
        return self.next(cc)
