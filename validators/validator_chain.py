from validators.cc_validator import CCValidator
from validators.correo_validator import CorreoValidator
from validators.nombre_validator import NombreValidator

def crear_cadena_validacion_cc(existing_ccs):
    # Cadena de validación para la cédula
    return CCValidator(existing_ccs)

def crear_cadena_validacion_nombre():
    # Cadena de validación para el nombre
    return NombreValidator()

def crear_cadena_validacion_correo():
    # Cadena de validación para el correo
    return CorreoValidator()
