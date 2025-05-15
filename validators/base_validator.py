from abc import ABC, abstractmethod

class Validator(ABC):
    def __init__(self):
        self._next_validator = None

    def set_next(self, validator):
        self._next_validator = validator
        return validator 

    @abstractmethod
    def validate(self, value, errors):
        pass

    def next(self, value, errors):
        if self._next_validator:
            return self._next_validator.validate(value, errors)
        return errors
