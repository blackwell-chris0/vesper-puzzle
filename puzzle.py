import math
from enum import Enum

class Operator(Enum):
    ADD = 1
    MULTIPLY = 2


def find_combination(target: int, operator: Operator) -> list:
    def backtrack(start: int, path: list, remaining: int, operator: Operator) -> list:
        if len(path) == 4:
            if (operator == Operator.ADD and remaining == 0) or (operator == Operator.MULTIPLY and remaining == 1):
                return path
            else:
                return None
        for num in range(start, 9):
            if operator == Operator.ADD:
                if remaining - num >= 0:
                    result = backtrack(num + 1, path + [num], remaining - num, operator)
                    if result:
                        return result
            elif operator == Operator.MULTIPLY:
                if remaining % num == 0:
                    result = backtrack(num + 1, path + [num], remaining // num, operator)
                    if result:
                        return result
        return None

    return backtrack(1, [], target, operator)


def find_closest_factors(input_value):
    closest_factors = None
    smallest_difference = float('inf')
    sqrt_input = int(math.sqrt(input_value))

    for i in range(1, sqrt_input + 1):
        if input_value % i == 0:
            factor1 = i
            factor2 = input_value // i
            difference = abs(factor1 - factor2)
            if difference < smallest_difference:
                smallest_difference = difference
                closest_factors = (factor1, factor2)

    return closest_factors



target_sum = 16
result = find_combination(target_sum, Operator.ADD)
print(f'Sum combination found: {result}')


target_product = 168
result = find_combination(target_product, Operator.MULTIPLY)
print(f'Product combination found: {result}')

input_value = 575
factors = find_closest_factors(input_value)
print('Factors:', factors)
for factor in factors:
    print(f'Sum combination found: {find_combination(factor, Operator.ADD)}')
