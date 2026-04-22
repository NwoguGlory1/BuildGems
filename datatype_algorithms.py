# Integer arithmetic – Write a function that takes an integer and returns the sum of all its digits.
# def sum_of_digits(x):
#     total = 0
#     for digit in str(x):
#         total += int(digit)
#     return total
def sum_of_digits(x):
    y = []
    for i in str(x):
        y.append(int(i))
    return (sum(y))
print(sum_of_digits(250))


# Float precision – Write a function that rounds a list of floats to 2 decimal places and returns the result.


# String reversal – Write a function that checks whether a string is a palindrome.

# def is_palindrome(x):
#     if x == x[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome("present"))

# # Boolean logic – Write a function that takes a list of booleans and returns True only if all values are True.
# def all_true(lst):
#     for item in lst:
#         if item == False:
#             return False
#     return True
# lst = [True, True, True]
# print(all_true(lst))

# List max without built-in – Write a function that finds the maximum value in a list without using max().