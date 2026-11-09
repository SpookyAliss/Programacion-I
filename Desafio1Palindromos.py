import unicodedata  #separa las letras base de sus tildes o marcas (por ejemplo, separa la "a" de la tilde en "á")


def _normalizar(texto: str) -> str:
    """Quita tildes y diéresis, conserva la ñ, y deja solo alfanuméricos en minúsculas."""
    descompuesto = unicodedata.normalize("NFD", texto)
    resultado = []
    for c in descompuesto:
        if unicodedata.category(c) == "Mn":
            # Conservar la tilde solo si forma una ñ/Ñ
            if c == "\u0303" and resultado and resultado[-1] in "nN":
                resultado.append(c)
            continue
        resultado.append(c)
    # Recomponer (n + ~ -> ñ) para que el reverso no separe la marca
    recompuesto = unicodedata.normalize("NFC", "".join(resultado))
    return "".join(c.casefold() for c in recompuesto if c.isalnum())


def es_palindromo(texto: str) -> bool:
    """Devuelve True si el texto es palíndromo (ignora espacios, puntuación,
    mayúsculas y acentos; conserva la ñ). Un texto sin alfanuméricos devuelve False."""
    if not isinstance(texto, str):
        raise TypeError("La entrada debe ser una cadena de texto.")
    limpio = _normalizar(texto)
    return bool(limpio) and limpio == limpio[::-1]


def main():
    print("=== Detector de Palíndromos como evaluación para la Tarea ===")
    print("Profesor, Osvaldo. Escribe una palabra o frase para evaluar. Si desea salir, presiona Ctrl+C.\n")
    try:
        while True:
            entrada = input("Ingresa tu texto: ")
            if not any(c.isalnum() for c in entrada):
                print("Ingresa al menos una letra o número.\n")
                continue
            if es_palindromo(entrada):
                print(f"{entrada}' sí es un palíndromo. Felicidades, Osvaldo.\n")
            else:
                print(f"{entrada}' nO es un palíndromo. Lo lamentamos, Osvaldo. \n")
    except (KeyboardInterrupt, EOFError):
        print("\n¡Hasta luego!")


if __name__ == "__main__":
    main()