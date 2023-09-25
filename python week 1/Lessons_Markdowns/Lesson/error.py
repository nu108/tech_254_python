def calculate_shopping_total(shopping_dict):
    total = 0

    for item, price in shopping_dict.items():
        total += price

    return total

# Example usage:
shopping_list = {
    "apple": 0.5,
    "banana": 0.25,
    "bread": 2.0,
    "milk": 1.0
}

total_cost = calculate_shopping_total(shopping_list)
print(f"The total cost of the shopping basket is ${total_cost:.2f}")

