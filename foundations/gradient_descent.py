class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        a = init

        for i in range(0, iterations):
            derivative = 2*a
            a = a - learning_rate*derivative
        
        return round(a, 5)

        pass
