# Desafío 2: Generador de Histograma

Módulo en Python que recibe una lista de números y dibuja un histograma
horizontal en la consola usando asteriscos.

## Características

- **Validación previa (fail fast):** revisa toda la lista antes de imprimir,
  de modo que nunca se muestra una salida parcial. Rechaza entradas que no
  sean lista, elementos no numéricos, booleanos (`True`/`False`), negativos,
  `NaN` e infinito.
- **Escalado automático:** si el valor máximo supera `ancho_max` (50 por
  defecto), las barras se escalan proporcionalmente y se indica la escala usada.
- **Alineación dinámica:** el ancho de las etiquetas se calcula según los
  datos, para que la barra vertical (`|`) quede alineada.
- **Valores positivos siempre visibles:** un valor mayor que 0 muestra al
  menos un asterisco; el 0 no muestra ninguno.
- **Errores claros:** los mensajes indican la posición del elemento inválido.
- **Pruebas integradas:** el script incluye casos normales y de error
  (`_debe_fallar`) que se ejecutan al correrlo.

## Requisitos

- Python 3.6 o superior.
- Sin dependencias externas (solo `math` y `typing`, de la biblioteca estándar).

## Cómo utilizarlo

### 1. Ejecución directa (Run Python File)

Al ejecutar el archivo se corre una batería de pruebas con casos normales,
flotantes, ceros, valores grandes, lista vacía y entradas inválidas.


## Ejemplo de salida

```
--- Histograma ---

 4 | ****
 9 | *********
 2 | **
15 | ***************
 7 | *******
```

Con valores grandes se escala y se avisa:

```
--- Histograma ---

100 | ********************
250 | **************************************************
 40 | ********

(Escala: cada '*' ≈ 5.00 unidades)
```

## Decisiones de diseño

- Se separa la validación (`_validar_datos`) de la salida, para no imprimir
  nada si hay un dato inválido.
- Se excluye `bool` de forma explícita porque en Python es subclase de `int`.
- El redondeo de las barras es el convencional (2.5 → 3), no el "al par" de `round()`.
- Una lista vacía muestra un aviso en lugar de lanzar una excepción.

## Excepciones

- `TypeError`: si `datos` no es una lista.
- `ValueError`: si hay elementos no numéricos, negativos, `NaN` o infinito,
  o si `ancho_max` no es un entero positivo.