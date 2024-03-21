import pytest
from valid_tel import validar_telefone

@pytest.mark.parametrize("numero_telefone, esperado", [
    ("(11) 98888-7777", True),
    ("(22) 7777-6666", True),
    ("(33) 99887766", False),  
    ("44 9999-9999", False),   
    ("(21)9 8765-4321", False),
    ("(00) 12345-6789", True),
    ("(85) 99999-9999", True), 
    ("(1) 9999-9999", False),  
    ("(123) 9999-9999", False),
    ("(99)9999-9999", False),  
    ("", False),               
    ("(99) 9999-999", False),  
    ("(99) 99999-99999", False)
])
def test_validacao_telefone(numero_telefone, esperado):
    assert validar_telefone(numero_telefone) == esperado, f"Erro ao validar {numero_telefone}"
