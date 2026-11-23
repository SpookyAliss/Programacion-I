# Desafío 3: Administrador de contactos

Programa de consola en Python para administrar una agenda de contactos. Cada contacto tiene nombre, teléfono y correo electrónico.

## Funcionalidades

1. Agregar un contacto nuevo
2. Ver la lista de contactos (ordenada alfabéticamente)
3. Buscar un contacto por nombre (coincidencia parcial, sin distinguir mayúsculas)
4. Eliminar un contacto por nombre

## Estructura de datos

- La agenda es una **lista de tuplas** `(clave, info)`.
- `clave` es el nombre normalizado (minúsculas, sin espacios extra) y se usa para comparar.
- `info` es un **diccionario** `{"nombre", "telefono", "correo"}`.

## Diseño

- Cada funcionalidad tiene su propia función de lógica (`agregar_contacto`, `listar_contactos`, `buscar_contactos`, `eliminar_contacto`), separada de la interacción con el usuario (`opcion_*`), lo que facilita probarlas.
- Un diccionario de acciones despacha las opciones del menú, evitando una cadena de `if/elif`.

## Robustez

- Validación de teléfono y correo con expresiones regulares.
- Nombres vacíos rechazados y duplicados detectados sin importar mayúsculas o espacios.
- Opciones de menú inválidas, `Ctrl+C` y `Ctrl+D` se manejan sin que el programa falle.

## Cómo ejecutarlo

```bash
python administrador_contactos.py
```

Requiere Python 3.6 o superior. No usa librerías externas.
