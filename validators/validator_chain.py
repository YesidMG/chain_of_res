from validators.cc_validator import CCValidator
from validators.correo_validator import CorreoValidator
from validators.nombre_validator import NombreValidator

def crear_cadena_validacion(existing_ccs):
    cc_validator = CCValidator(existing_ccs)
    nombre_validator = NombreValidator()
    correo_validator = CorreoValidator()

    # Enlazamos: CC -> Nombre -> Correo
    cc_validator.set_next(nombre_validator).set_next(correo_validator)
    return cc_validator
