def find_combination(target_product):
    def backtrack(start, path, remaining_product):
        if len(path) == 4:
            if remaining_product == 1:
                return path
            else:
                return None
        for num in range(start, 9):
            if remaining_product % num == 0:
                result = backtrack(num + 1, path + [num], remaining_product // num)
                if result:
                    return result
        return None

    return backtrack(1, [], target_product)

# Example usage:
target_product = 168
result = find_combination(target_product)
if result:
    print(f"Combination found: {result}")
else:
    print(f"No combination found that multiplies to {target_product}")
