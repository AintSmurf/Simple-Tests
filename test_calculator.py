from calculator import calculator
import pytest

def test_add_3plus5_returns8():

    #arrange
    actual = 8
    expected = 0
    c = calculator()

    #act
    expected = c.add(3,5)

    #assert
    assert actual == expected
def test_minus_3minus5_returnsminus2():

    #arrange
    actual = -2
    expected = 0
    c = calculator()

    #act
    expected = c.minus(3,5)

    #assert
    assert actual == expected
def test_multiply_3multiply5_returns15():

    #arrange
    actual = 15
    expected = 0
    c = calculator()

    #act
    expected = c.multiply(3,5)

    # assert
    assert actual == expected
def test_divide_4divide2_returns2():

    #arrange
    actual = 2
    expected = 0
    c = calculator()

    #act
    expected = c.divide(4,2)

    # assert
    assert actual == expected