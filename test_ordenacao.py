import pytest
from ordenacao import ordenar_crescente, ordenar_decrescente

def test_ordenar_crescente():
    assert ordenar_crescente([5, 2, 3, 1, 4]) == [1, 2, 3, 4, 5], "A lista deve estar ordenada em ordem crescente"
    assert ordenar_crescente([]) == [], "A lista vazia deve retornar uma lista vazia"
    assert ordenar_crescente([1]) == [1], "Uma lista com um único elemento deve retornar ela mesma"
    assert ordenar_crescente([1, 1, 1]) == [1, 1, 1], "Uma lista com elementos iguais deve retornar ela mesma"
    assert ordenar_crescente([-1, -2, -3]) == [-3, -2, -1], "A lista com números negativos deve ser ordenada corretamente"

def test_ordenar_decrescente():
    assert ordenar_decrescente([5, 2, 3, 1, 4]) == [5, 4, 3, 2, 1], "A lista deve estar ordenada em ordem decrescente"
    assert ordenar_decrescente([]) == [], "A lista vazia deve retornar uma lista vazia"
    assert ordenar_decrescente([1]) == [1], "Uma lista com um único elemento deve retornar ela mesma"
    assert ordenar_decrescente([1, 1, 1]) == [1, 1, 1], "Uma lista com elementos iguais deve retornar ela mesma"
    assert ordenar_decrescente([-1, -2, -3]) == [-1, -2, -3], "A lista com números negativos deve ser ordenada corretamente em ordem decrescente"
