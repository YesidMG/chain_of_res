from abc import ABC, abstractmethod

class Validator(ABC):
    def __init__(self):
        self._next_validator = None

    def set_next(self, validator):
        self._next_validator = validator
        return validator  # Para encadenar fácilmente

    @abstractmethod
    def validate(self, value):
        pass

    def next(self, value):
        if self._next_validator:
            return self._next_validator.validate(value)
        return True
