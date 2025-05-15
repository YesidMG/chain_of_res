from services.persona_service import PersonaService
from services.evento_service import EventoService
from validators.validator_chain import crear_cadena_validacion
from datetime import datetime

def registrar_persona(persona_service):
    print("\n--- Registrar Persona ---")
    cc = input("Cédula: ").strip()
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip()
    direccion = input("Dirección: ").strip()

    existing_ccs = {p.cc for p in persona_service.personas}
    cadena_validacion = crear_cadena_validacion(existing_ccs)

    if not cadena_validacion.validate(cc):
        return
    if not cadena_validacion.validate(nombre):
        return
    if not cadena_validacion.validate(correo):
        return

    if persona_service.existe_cc(cc):
        print("Error: Ya existe una persona con esa cédula.")
        return

    persona_service.registrar_persona(cc, nombre, telefono, correo, direccion)

def listar_personas(persona_service):
    print("\n--- Lista de Personas ---")
    persona_service.listar_personas()

def buscar_persona(persona_service):
    print("\n--- Buscar Persona por Cédula ---")
    cc = input("Ingrese cédula: ").strip()
    persona = persona_service.buscar_por_cc(cc)
    if persona:
        print(persona)
    else:
        print("Persona no encontrada.")

def registrar_evento(persona_service, evento_service):
    print("\n--- Registrar Evento ---")

    if len(persona_service.personas) == 0:
        print("No hay personas registradas. Debe registrar al menos una persona antes de crear un evento.")
        return

    nombre = input("Nombre del evento: ").strip()
    direccion = input("Dirección: ").strip()
    fecha_str = input("Fecha (YYYY-MM-DD): ").strip()

    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
    except ValueError:
        print("Formato de fecha inválido.")
        return

    cc_duenio = input("Cédula del dueño del evento: ").strip()
    duenio = persona_service.buscar_por_cc(cc_duenio)
    if not duenio:
        print("No existe persona con esa cédula como dueño.")
        return

    descripcion = input("Descripción del evento: ").strip()

    evento = evento_service.registrar_evento(nombre, direccion, fecha, cc_duenio, descripcion)
    if not evento:
        return

    # Registrar personal para el evento
    while True:
        agregar = input("¿Desea agregar personal al evento? (s/n): ").lower()
        if agregar != 's':
            break

        cc_persona = input("Cédula de la persona para asignar: ").strip()
        persona = persona_service.buscar_por_cc(cc_persona)
        if not persona:
            print("Persona no encontrada.")
            seguir = input("¿Buscar otra persona? (s/n): ").lower()
            if seguir != 's':
                break
            else:
                continue
        else:
            print(persona)
            registrar = input("¿Registrar esta persona al evento? (s/n): ").lower()
            if registrar == 's':
                rol = input("Ingrese rol/trabajo de la persona en el evento: ").strip()
                evento_service.asignar_personal(evento, cc_persona, rol)
            seguir = input("¿Buscar otra persona para asignar? (s/n): ").lower()
            if seguir != 's':
                break

def listar_eventos(evento_service):
    print("\n--- Lista de Eventos ---")
    evento_service.listar_eventos()

def buscar_evento(evento_service):
    print("\n--- Buscar Evento por ID ---")
    try:
        id_evento = int(input("Ingrese ID del evento: "))
    except ValueError:
        print("ID inválido.")
        return

    evento = evento_service.buscar_evento_por_id(id_evento)
    if evento:
        print(evento)
    else:
        print("Evento no encontrado.")

def main():
    persona_service = PersonaService()
    evento_service = EventoService(persona_service)

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Persona")
        print("2. Listar Personas")
        print("3. Buscar Persona por Cédula")
        print("4. Registrar Evento")
        print("5. Listar Eventos")
        print("6. Buscar Evento por ID")
        print("7. Terminar")
        opcion = input("Seleccione opción: ").strip()

        if opcion == '1':
            registrar_persona(persona_service)
        elif opcion == '2':
            listar_personas(persona_service)
        elif opcion == '3':
            buscar_persona(persona_service)
        elif opcion == '4':
            registrar_evento(persona_service, evento_service)
        elif opcion == '5':
            listar_eventos(evento_service)
        elif opcion == '6':
            buscar_evento(evento_service)
        elif opcion == '7':
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()