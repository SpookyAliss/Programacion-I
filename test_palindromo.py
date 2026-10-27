import pytest
from Desafio1Palindromos import es_palindromo

@pytest.mark.parametrize("texto, esperado", [
    ("Anita lava la tina", True),
    ("A man, a plan, a canal: Panama", True),
    ("Átale, demoníaco Caín, o me delata", True),
    ("ñan", False),
    ("hola", False),
    ("a", True),
    ("...", False),
    ("12321", True),
])
def test_es_palindromo(texto, esperado):
    assert es_palindromo(texto) == esperado

def test_tipo_invalido():
    with pytest.raises(TypeError):
        es_palindromo(123)