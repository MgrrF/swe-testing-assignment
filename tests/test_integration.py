from calculator.calc import Calculator

def test_full_addition_flow():
    """
    Simulates a user adding two numbers: 5 + 3 = 8
    """
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_clear_resets_calculator():
    """
    Simulates a user pressing Clear after a calculation
    """
    calc = Calculator()
    calc.add(10, 5)       # do some calculation
    cleared = calc.clear() # user presses Clear
    assert cleared == 0
