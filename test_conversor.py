import pytest
import conversor

def test_dolar_para_euro():
    assert conversor.dolar_para_euro(100) == pytest.approx(93)

def test_euro_para_dolar():
    assert conversor.euro_para_dolar(100) == pytest.approx(108)

def test_real_para_dolar():
    assert conversor.real_para_dolar(100) == pytest.approx(20)

def test_dolar_para_real():
    assert conversor.dolar_para_real(100) == pytest.approx(500)

def test_euro_para_real():
    assert conversor.euro_para_real(100) == pytest.approx(538)

def test_real_para_euro():
    assert conversor.real_para_euro(100) == pytest.approx(19)
