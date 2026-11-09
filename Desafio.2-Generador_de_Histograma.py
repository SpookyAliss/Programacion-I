import math
from typing import List, Union

Numero = Union[int, float]


def _validar_datos(datos: list) -> None:
    """Valida toda la entrada antes de imprimir nada."""
    if not isinstance(datos, list):
        raise TypeError("El argumento proporcionado debe ser una lista.")

    for i, valor in enumerate(datos):
        # bool es subclase de int, así que se excluye de forma explícita
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError(
                f"Elemento en posición {i} inválido ({valor!r}): debe ser un número."
            )
        if isinstance(valor, float) and not math.isfinite(valor):
            raise ValueError(
                f"Elemento en posición {i} inválido ({valor!r}): debe ser finito."
            )
        if valor < 0:
            raise ValueError(
                f"Elemento en posición {i} inválido ({valor!r}): no puede ser negativo."
            )


def generar_histograma(datos: List[Numero], ancho_max: int = 50) -> None:
    """
    Genera un histograma horizontal en consola usando asteriscos.

    Parámetros:
        datos: lista de números (int o float) no negativos.
        ancho_max: longitud máxima de la barra más larga. Si el valor máximo
                   cabe en ese ancho, se dibuja a escala 1:1; si no, se
                   escala proporcionalmente.

    Excepciones:
        TypeError: si `datos` no es una lista.
        ValueError: si hay elementos no numéricos, negativos, NaN/inf,
                    o si `ancho_max` no es un entero positivo.
    """
    if not isinstance(ancho_max, int) or isinstance(ancho_max, bool) or ancho_max < 1:
        raise ValueError("ancho_max debe ser un entero positivo.")

    _validar_datos(datos)

    if not datos:
        print("La lista está vacía. No hay nada que graficar.")
        return

    maximo = max(datos)
    # Escala 1:1 si cabe; si no, se reduce proporcionalmente
    escala = min(1.0, ancho_max / maximo) if maximo > 0 else 1.0
    ancho_etiqueta = max(len(str(d)) for d in datos)

    print("\n--- Histograma ---\n")
    for valor in datos:
        largo = int(valor * escala + 0.5)
        if valor > 0:
            largo = max(1, largo)
        barra = "*" * largo
        print(f"{valor:>{ancho_etiqueta}} | {barra}")
    print()
    if escala < 1.0:
        print(f"(Escala: cada '*' ≈ {1 / escala:.2f} unidades)")


# ==========================================
# Pruebas
# ==========================================
def _debe_fallar(datos, excepcion):
    try:
        generar_histograma(datos)
    except excepcion:
        print(f"  OK: {datos!r} lanzó {excepcion.__name__}")
    else:
        raise AssertionError(f"{datos!r} debía lanzar {excepcion.__name__}")


if __name__ == "__main__":
    print("Prueba 1: lista normal")
    generar_histograma([4, 9, 2, 15, 7])

    print("Prueba 2: flotantes")
    generar_histograma([3.8, 5.1, 8.9])

    print("Prueba 3: con ceros")
    generar_histograma([0, 3, 0, 5])

    print("Prueba 4: valores grandes (se escala)")
    generar_histograma([100, 250, 40])

    print("Prueba 5: lista vacía")
    generar_histograma([])

    print("Pruebas de robustez:")
    _debe_fallar("no es una lista", TypeError)
    _debe_fallar([3, "cuatro", 5], ValueError)
    _debe_fallar([4, -2, 5], ValueError)
    _debe_fallar([True, 3], ValueError)
    _debe_fallar([float("nan"), 3], ValueError)
    _debe_fallar([float("inf")], ValueError)