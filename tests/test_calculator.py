from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 10
        b = 25
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 35
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 25
        b = 10
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 15
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 10
        b = 5
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 50
        assert result == expected

    def test_divide(self):
        # arrange
        a = 10
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 5
        assert result == expected

    def test_divide_by_zero(self):
        # arrange
        a = 10
        b = 0
        cal = Calculator()

        with pytest.raises(ZeroDivisionError) as e:
            # act
            cal.divide(a, b)
        assert str(e.value) == "Division by zero error"