"""
Desafío 3: Administrador de contactos

Crea un programa que permita administrar una lista de contactos. Cada contacto deberá tener un
nombre, un número de teléfono y una dirección de correo electrónico. El programa deberá ofrecer las
siguientes funcionalidades:

1. Agregar un contacto nuevo
2. Ver la lista de contactos
3. Buscar un contacto por nombre
4. Eliminar un contacto por nombre

Usa listas y tuplas para almacenar los contactos y un diccionario para almacenar la información de cada
contacto. También deberás crear distintas funciones para cada una de las funcionalidades.

Estructura de datos:
    - La agenda es una LISTA de TUPLAS (clave, info).
    - `clave` es el nombre normalizado (sin mayúsculas ni espacios extra) y
      sirve para comparar nombres de forma consistente.
    - `info` es un DICCIONARIO con los datos del contacto:
      {"nombre": ..., "telefono": ..., "correo": ...}
"""

import re

# Validaciones simples pero razonables para teléfono y correo.
DIG_TELEFONO = re.compile(r"^\+?[\d\s\-()]{10,16}$")
DIG_CORREO = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")


# ---------------------------------------------------------------------------
# Lógica (sin input/print, para que sea fácil de probar)
# ---------------------------------------------------------------------------
def normalizar(texto):
    """Quita espacios sobrantes y pasa a minúsculas para comparar nombres."""
    return " ".join(texto.split()).casefold()


def agregar_contacto(contactos, nombre, telefono, correo):
    """Agrega un contacto. Lanza ValueError si los datos no son válidos
    o si el nombre ya existe."""
    nombre = " ".join(nombre.split())
    telefono = telefono.strip()
    correo = correo.strip()

    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    if not DIG_TELEFONO.match(telefono):
        raise ValueError("Teléfono inválido (10 a 16 dígitos; se permiten +, espacios, - y paréntesis).")
    if not DIG_CORREO.match(correo):
        raise ValueError("Correo electrónico inválido.")

    clave = normalizar(nombre)
    if any(c == clave for c, _ in contactos):
        raise ValueError(f"Ya existe un contacto llamado '{nombre}'.")

    info = {"nombre": nombre, "telefono": telefono, "correo": correo}
    contactos.append((clave, info))


def listar_contactos(contactos):
    """Devuelve la lista de contactos (dicts) ordenada alfabéticamente."""
    return [info for _, info in sorted(contactos, key=lambda c: c[0])]


def buscar_contactos(contactos, termino):
    """Devuelve los contactos cuyo nombre contiene el término (sin distinguir
    mayúsculas). Permite búsquedas parciales como 'ana'."""
    termino = normalizar(termino)
    if not termino:
        return []
    return [info for clave, info in contactos if termino in clave]


def eliminar_contacto(contactos, nombre):
    """Elimina el contacto con ese nombre exacto (sin distinguir mayúsculas).
    Devuelve True si lo eliminó, False si no existía."""
    clave = normalizar(nombre)
    for i, (c, _) in enumerate(contactos):
        if c == clave:
            del contactos[i]
            return True
    return False


# ---------------------------------------------------------------------------
# Interfaz de consola
# ---------------------------------------------------------------------------
def mostrar_contacto(info):
    print(f"  Nombre:   {info['nombre']}")
    print(f"  Teléfono: {info['telefono']}")
    print(f"  Correo:   {info['correo']}")


def opcion_agregar(contactos):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    try:
        agregar_contacto(contactos, nombre, telefono, correo)
        print("✔ Contacto agregado.")
    except ValueError as error:
        print(f"✘ No se pudo agregar: {error}")


def opcion_listar(contactos):
    lista = listar_contactos(contactos)
    if not lista:
        print("La agenda está vacía.")
        return
    print(f"\n--- {len(lista)} contacto(s) ---")
    for info in lista:
        mostrar_contacto(info)
        print()


def opcion_buscar(contactos):
    termino = input("Nombre a buscar: ")
    resultados = buscar_contactos(contactos, termino)
    if not resultados:
        print("No se encontraron contactos.")
        return
    print(f"\n--- {len(resultados)} resultado(s) ---")
    for info in resultados:
        mostrar_contacto(info)
        print()


def opcion_eliminar(contactos):
    nombre = input("Nombre exacto del contacto a eliminar: ")
    if eliminar_contacto(contactos, nombre):
        print("✔ Contacto eliminado.")
    else:
        print("✘ No existe un contacto con ese nombre.")


def main():
    contactos = []  # lista de tuplas (clave, dict)
    acciones = {
        "1": opcion_agregar,
        "2": opcion_listar,
        "3": opcion_buscar,
        "4": opcion_eliminar,
    }
    menu = (
        "\n=== Administrador de contactos ===\n"
        "1. Agregar contacto\n"
        "2. Ver lista de contactos\n"
        "3. Buscar contacto por nombre\n"
        "4. Eliminar contacto por nombre\n"
        "5. Salir"
    )
    try:
        while True:
            print(menu)
            opcion = input("Elige una opción: ").strip()
            if opcion == "5":
                print("¡Hasta luego!")
                break
            accion = acciones.get(opcion)
            if accion:
                accion(contactos)
            else:
                print("Opción no válida, intenta de nuevo.")
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma terminado.")


if __name__ == "__main__":
    main()
