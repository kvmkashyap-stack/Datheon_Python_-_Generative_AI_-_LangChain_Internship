import pytest
from tools.calculator import calculate

def test_addition():
    assert calculate("10 + 5") == 15

def test_multiplication():
    assert calculate("458 * 239") == 109462

def test_subtraction():
    assert calculate("10 - 5") == 5

def test_operator_precedence():
    assert calculate("2 + 3 * 4") == 14

def test_power():
    assert calculate("2 ** 10") == 1024

def test_division_by_zero():
    with pytest.raises(ValueError):
        calculate("10 / 0")

def test_rejects_python_code():
    with pytest.raises(ValueError):
        calculate("__import__('os').system('echo unsafe')")

def test_rejects_empty_expression():
    with pytest.raises(ValueError):
        calculate("   ")
