from validators.cc_validator import CCValidator
from validators.correo_validator import CorreoValidator
from validators.nombre_validator import NombreValidator

def crear_cadena_validacion_cc(existing_ccs):
    return CCValidator(existing_ccs)

def crear_cadena_validacion_nombre():
    return NombreValidator()

def crear_cadena_validacion_correo():
    return CorreoValidator()
