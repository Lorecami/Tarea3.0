import pytest
from app import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(5, 3) == 8

def test_restar():
    assert restar(5, 3) == 2

def test_multiplicar():
    assert multiplicar(5, 3) == 15

def test_dividir():
    assert dividir(6, 2) == 3

def test_dividir_para_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)