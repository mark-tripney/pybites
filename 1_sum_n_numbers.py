# Write a function that can sum up numbers:
#
# It should receive a sequence of n numbers.
# If no argument is provided, return sum of numbers 1..100.
# Look closely to the type of the function's default argument ...


def sum_numbers(numbers=None):
    if numbers is None:
        return sum(range(1, 101))
    return sum(numbers)
