import pytest [cite: 238]
from src.calculator import Calculator [cite: 239]

# Cung cấp một instance Calculator dùng chung cho các test [cite: 240]
@pytest.fixture [cite: 241]
def calc(): [cite: 242]
    return Calculator() [cite: 243]

class TestAddition: [cite: 245]
    def test_add_two_positive_numbers(self, calc): [cite: 246]
        assert calc.add(3, 5) == 8 [cite: 246]

    def test_add_negative_numbers(self, calc): [cite: 247]
        assert calc.add(-3, -5) == -8 [cite: 248]

    def test_add_positive_and_negative(self, calc): [cite: 249]
        assert calc.add(10, -3) == 7 [cite: 250]

    def test_add_with_zero(self, calc): [cite: 251]
        assert calc.add(5, 0) == 5 [cite: 252, 253]

    def test_add_floats(self, calc): [cite: 254]
        assert abs(calc.add(1.5, 2.3) - 3.8) < 0.0001 [cite: 255]

class TestSubtraction: [cite: 257]
    def test_subtract_basic(self, calc): [cite: 258]
        assert calc.subtract(10, 4) == 6 [cite: 259]

    def test_subtract_resulting_negative(self, calc): [cite: 260]
        assert calc.subtract(3, 10) == -7 [cite: 261]

class TestMultiplication: [cite: 263]
    def test_multiply_basic(self, calc): [cite: 265]
        assert calc.multiply(4, 5) == 20 [cite: 265]

    def test_multiply_by_zero(self, calc): [cite: 266]
        assert calc.multiply(100, 0) == 0 [cite: 266]

    def test_multiply_negatives(self, calc): [cite: 267]
        assert calc.multiply(-3, -4) == 12 [cite: 267]

class TestDivision: [cite: 269]
    def test_divide_basic(self, calc): [cite: 270]
        assert calc.divide(10, 2) == 5 [cite: 271]

    def test_divide_resulting_float(self, calc): [cite: 272]
        assert calc.divide(7, 2) == 3.5 [cite: 273]

    def test_divide_by_zero_raises_error(self, calc): [cite: 274]
        with pytest.raises(ValueError, match='Cannot divide by zero'): [cite: 275]
            calc.divide(10, 0) [cite: 276]

class TestOtherOperations: [cite: 278]
    def test_power_basic(self, calc): [cite: 279]
        assert calc.power(2, 10) == 1024 [cite: 280]

    def test_power_zero_exponent(self, calc): [cite: 281]
        assert calc.power(999, 0) == 1 [cite: 281]

    def test_is_positive_true(self, calc): [cite: 282]
        assert calc.is_positive(5) == True [cite: 282]

    def test_is_positive_false(self, calc): [cite: 283]
        assert calc.is_positive(-1) == False [cite: 283]

    def test_is_positive_zero(self, calc): [cite: 284]
        assert calc.is_positive(0) == False [cite: 284]