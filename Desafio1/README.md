# Desafío 1: Verificador de Palíndromos 

## Objetivo del Desafío
Crear un programa en Python que reciba una cadena de texto por parte del usuario y determine si es un palíndromo. El programa debe ser capaz de ignorar espacios, signos de puntuación y capitalización.

## Solución Propuesta
La solución se implementó en `Desafio1Palindromos.py` enfocándose en los siguientes pilares:
- **Funcionalidad:** Identifica correctamente palíndromos estándar.
- **Robustez:** Implementa `unicodedata` para soportar vocales con tildes (acentos diacríticos) muy comunes en el idioma español, y cuenta con un bloque `try-except` para manejar interrupciones del teclado.
- **Eficiencia:** Utiliza *List Comprehension* y *Slicing* (`[::-1]`), que son técnicas nativas de Python optimizadas.
- **Legibilidad:** El código está tipado (`Type Hints`) y documentado con *Docstrings*.

## Cómo ejecutarlo
Asegurarse de tener Python 3.x instalado. Ejecuta el siguiente comando en tu terminal:

```bash
python Desafio1Palindromos.py
