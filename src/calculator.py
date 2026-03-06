class Calculator:
    """Class performing basic mathematical operations.""" [cite: 220]

    def add(self, a: float, b: float) -> float:
        """Add two numbers.""" [cite: 222]
        return a + b [cite: 223]

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a.""" [cite: 224]
        return a - b [cite: 225]

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers.""" [cite: 227]
        return a * b [cite: 227]

    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Raises ValueError if b=0.""" [cite: 229]
        if b == 0: [cite: 229]
            raise ValueError('Cannot divide by zero!') [cite: 230]
        return a / b [cite: 230]

    def power(self, base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent.""" [cite: 233]
        return base ** exponent [cite: 233, 234]

    def is_positive(self, n: float) -> bool:
        """Check if a number is positive.""" [cite: 235]
        return n > 0 [cite: 235]