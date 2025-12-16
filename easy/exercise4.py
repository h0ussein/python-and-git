# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.


def is_number_in_list(numbers, num):
    if num in numbers:
        return True
    else:
        return False


a = [1, 3, 5, 7, 9]
check = 10

result = is_number_in_list(a, check)
print(result)
